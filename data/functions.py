import streamlit as st
import sqlite3 as sql
from datetime import datetime, timedelta

######################################################################
# CRUD Operations
######################################################################

# Delete a booking by ID
def delete_booking(booking_id):

    success_msg = ""
    error_msg = ""
    try:
        with sql.connect(st.session_state.db_path) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
            con.commit()
            success_msg = "Booking record successfully deleted!"
    except Exception as e:
        con.rollback()
        error_msg = f"Error deleting record: {e}"
    return success_msg, error_msg

# Update a booking by ID
def update_booking(booking_id, **kwargs):

    success_msg = ""
    error_msg = ""
    try:
        with sql.connect(st.session_state.db_path) as con:
            cur = con.cursor()
            # Build the SET clause dynamically
            set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
            values = list(kwargs.values())
            values.append(booking_id)
            cur.execute(f"UPDATE bookings SET {set_clause} WHERE booking_id = ?", values)
            con.commit()
            success_msg = "Booking record successfully updated!"
    except Exception as e:
        con.rollback()
        error_msg = f"Error updating record: {e}"
    return success_msg, error_msg

# Get all bookings
def get_bookings():

    with sql.connect(st.session_state.db_path) as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM bookings")
        rows = cur.fetchall()
    return rows

# Add a new booking
def add_booking(guest_name,hotel_type, check_in, check_out,
                        num_adults, num_children, num_babies, special_requests, parking,
                        meal, country, room_type, deposit_type, customer_type,
                        average_daily_rate, assigned_room_type, market_segment,
                        distribution_channel, booking_changes, is_repeated_guest,
                        previous_cancellations, previous_bookings_not_canceled, prediction_score):

    success_msg = ""
    error_msg = ""  
    reservation_status = "Active"
    current_date = datetime.now()

    # Calculate lead_time automatically based on current date and check-in date
    if check_in:
        check_in_date = check_in if isinstance(check_in, datetime) else datetime.strptime(str(check_in), '%Y-%m-%d')      
        lead_time = (check_in_date.date() - current_date.date()).days
        lead_time = max(0, lead_time)  # Ensure lead_time is not negative
    else:
        lead_time = 0


    # Calculate stays in weekend and week nights
    if check_in and check_out:
        check_in_date = check_in if isinstance(check_in, datetime) else datetime.strptime(str(check_in), '%Y-%m-%d')
        check_out_date = check_out if isinstance(check_out, datetime) else datetime.strptime(str(check_out), '%Y-%m-%d')
        
        total_nights = (check_out_date - check_in_date).days
        weekend_nights = 0
        week_nights = 0

        check = check_in_date
        for _ in range(total_nights):
            if check.weekday() >= 5:  # Saturday (5) or Sunday (6)
                weekend_nights += 1
            else:
                week_nights += 1
            check += timedelta(days=1)
    else:
        weekend_nights = 0
        week_nights = 0
    try:
        with sql.connect(st.session_state.db_path) as con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO bookings (
                    booking_date, guest_name, check_in_date, check_out_date, lead_time, hotel_type,
                    stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, meal, country,
                    market_segment, distribution_channel, is_repeated_guest, previous_cancellations,
                    previous_bookings_not_canceled, reserved_room_type, assigned_room_type, booking_changes,
                    deposit_type, customer_type, adr, required_car_parking_spaces, total_of_special_requests,
                    reservation_status, reservation_status_date, cancellation_prob
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                current_date, guest_name, check_in, check_out, lead_time, hotel_type,
                weekend_nights, week_nights, num_adults, num_children, num_babies, meal, country,
                market_segment, distribution_channel, is_repeated_guest, previous_cancellations,
                previous_bookings_not_canceled, room_type, assigned_room_type, booking_changes,
                deposit_type, customer_type, average_daily_rate, parking, special_requests,
                reservation_status, current_date, prediction_score
            ))
            con.commit()
        success_msg = "Booking created successfully!"
    except Exception as e:
        con.rollback()
        error_msg = f"Error creating booking: {e}"
    return success_msg, error_msg

######################################################################
# Filtering Operations
######################################################################

def filter_bookings(bookings, search_query=None, status_filter=None, hotel_type_filter=None, date_filter=None):
    """Filter bookings based on various criteria"""
    filtered_bookings = bookings.copy()
    
    # Apply search filter
    if search_query:
        search_lower = search_query.lower()
        filtered_bookings = [
            booking for booking in filtered_bookings
            if (search_lower in str(booking['booking_id']) or
                search_lower in booking['guest_name'].lower() or
                search_lower in booking['hotel_type'].lower())
        ]
    
    # Apply status filter
    if status_filter and status_filter != "All":
        filtered_bookings = [
            booking for booking in filtered_bookings
            if booking['status'] == status_filter
        ]
    
    # Apply hotel type filter
    if hotel_type_filter and hotel_type_filter != "All":
        filtered_bookings = [
            booking for booking in filtered_bookings
            if booking['hotel_type'] == hotel_type_filter
        ]
    
    # Apply date range filter
    if date_filter and date_filter != "All":
        today = datetime.now()
    
        if date_filter == "This Week":
            start_date = today - timedelta(days=today.weekday())
            end_date = start_date + timedelta(days=6)
        elif date_filter == "This Month":
            start_date = today.replace(day=1)
            if today.month == 12:
                end_date = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
            else:
                end_date = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
        elif date_filter == "Next Month":
            if today.month == 12:
                start_date = today.replace(year=today.year + 1, month=1, day=1)
                end_date = today.replace(year=today.year + 1, month=2, day=1) - timedelta(days=1)
            else:
                start_date = today.replace(month=today.month + 1, day=1)
                end_date = today.replace(month=today.month + 2, day=1) - timedelta(days=1)

        filtered_bookings = [
            booking for booking in filtered_bookings
            if start_date <= datetime.strptime(booking['check_in'], '%Y-%m-%d') <= end_date
        ]
    
    return filtered_bookings 