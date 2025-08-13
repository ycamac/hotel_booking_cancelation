import sqlite3

conn = sqlite3.connect('./db/hotelligence.db')
print("Opened database successfully")

conn.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_date DATE NOT NULL,
    guest_name TEXT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    lead_time INTEGER NOT NULL,
    hotel_type TEXT NOT NULL,
    stays_in_weekend_nights INTEGER NOT NULL,
    stays_in_week_nights INTEGER NOT NULL,
    adults INTEGER NOT NULL,
    children INTEGER NOT NULL,
    babies INTEGER NOT NULL,
    meal TEXT NOT NULL,
    country TEXT NOT NULL,
    market_segment TEXT NOT NULL,
    distribution_channel TEXT NOT NULL,
    is_repeated_guest INTEGER NOT NULL,
    previous_cancellations INTEGER NOT NULL,
    previous_bookings_not_canceled INTEGER NOT NULL,
    reserved_room_type TEXT NOT NULL,
    assigned_room_type TEXT NOT NULL,
    booking_changes INTEGER NOT NULL,
    deposit_type TEXT NOT NULL,
    customer_type TEXT NOT NULL,
    adr REAL NOT NULL,
    required_car_parking_spaces INTEGER NOT NULL,
    total_of_special_requests INTEGER NOT NULL,
    reservation_status TEXT,
    reservation_status_date DATE,
    cancellation_prob REAL)''')

print("Hotel bookings table created successfully")
conn.close()