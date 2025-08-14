import sqlite3 as sql
from datetime import datetime, timedelta

def delete_booking(booking_id):
    db_path = "./db/hotelligence.db"
    success_msg = ""
    error_msg = ""
    try:
        with sql.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
            con.commit()
            success_msg = "Booking record successfully deleted!"
    except Exception as e:
        con.rollback()
        error_msg = f"Error deleting record: {e}"
    return success_msg, error_msg


def get_all_bookings():
    db_path = "./db/hotelligence.db"
    with sql.connect(db_path) as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM bookings")
        rows = cur.fetchall()
    return rows


def add_booking(guest_name,hotel_type, check_in, check_out,
                        num_adults, num_children, num_babies, special_requests, parking,
                        meal, country, room_type, deposit_type, customer_type,
                        average_daily_rate, assigned_room_type, market_segment,
                        distribution_channel, booking_changes, is_repeated_guest,
                        previous_cancellations, previous_bookings_not_canceled, prediction_score):


    db_path = "./db/hotelligence.db"    
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
        with sql.connect(db_path) as con:
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
        success_msg = "Booking record successfully added!"
    except Exception as e:
        con.rollback()
        error_msg = f"Error inserting record: {e}"
    return success_msg, error_msg


def delete_booking(booking_id):
    db_path = "./db/hotelligence.db"
    success_msg = ""
    error_msg = ""
    try:
        with sql.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
            con.commit()
            success_msg = "Booking record successfully deleted!"
    except Exception as e:
        con.rollback()
        error_msg = f"Error deleting record: {e}"
    return success_msg, error_msg