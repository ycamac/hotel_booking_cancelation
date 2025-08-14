import numpy as np
from datetime import datetime, timedelta

def generate_dummy_bookings():
    """Generate dummy booking data"""
    bookings = [
        {
            'booking_id': '#12345',
            'guest_name': 'Sophia Clark',
            'check_in': '2024-08-15',
            'check_out': '2024-08-20',
            'hotel_type': 'Deluxe Suite',
            'status': 'Confirmed',
            'prediction_score': 85
        },
        {
            'booking_id': '#12346',
            'guest_name': 'Ethan Bennett',
            'check_in': '2024-08-16',
            'check_out': '2024-08-18',
            'hotel_type': 'Standard Room',
            'status': 'Cancelled',
            'prediction_score': 20
        },
        {
            'booking_id': '#12347',
            'guest_name': 'Olivia Carter',
            'check_in': '2024-08-17',
            'check_out': '2024-08-22',
            'hotel_type': 'Family Room',
            'status': 'Confirmed',
            'prediction_score': 90
        },
        {
            'booking_id': '#12348',
            'guest_name': 'Liam Davis',
            'check_in': '2024-08-18',
            'check_out': '2024-08-21',
            'hotel_type': 'Deluxe Suite',
            'status': 'Confirmed',
            'prediction_score': 75
        },
        {
            'booking_id': '#12349',
            'guest_name': 'Ava Evans',
            'check_in': '2024-08-19',
            'check_out': '2024-08-23',
            'hotel_type': 'Standard Room',
            'status': 'Confirmed',
            'prediction_score': 60
        },
        {
            'booking_id': '#12350',
            'guest_name': 'Noah Foster',
            'check_in': '2024-08-20',
            'check_out': '2024-08-25',
            'hotel_type': 'Family Room',
            'status': 'Confirmed',
            'prediction_score': 95
        },
        {
            'booking_id': '#12351',
            'guest_name': 'Isabella Green',
            'check_in': '2024-08-21',
            'check_out': '2024-08-24',
            'hotel_type': 'Deluxe Suite',
            'status': 'Cancelled',
            'prediction_score': 10
        }
    ]
    return bookings

def create_new_booking(guest_name, hotel_type, check_in, check_out):
    """Create a new booking with prediction"""
    prediction_score = np.random.randint(10, 95)
    
    # Handle date conversion safely
    try:
        check_in_str = check_in.strftime('%Y-%m-%d') if check_in else ''
    except:
        check_in_str = str(check_in) if check_in else ''
    
    try:
        check_out_str = check_out.strftime('%Y-%m-%d') if check_out else ''
    except:
        check_out_str = str(check_out) if check_out else ''
    
    new_booking = {
        'booking_id': f'#{np.random.randint(10000, 99999)}',
        'guest_name': guest_name,
        'check_in': check_in_str,
        'check_out': check_out_str,
        'hotel_type': hotel_type,
        'status': 'Confirmed',
        'prediction_score': prediction_score
    }
    
    return new_booking, prediction_score

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