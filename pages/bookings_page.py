import streamlit as st
from data.bookings_data import generate_dummy_bookings, filter_bookings

def bookings_page():
    """Bookings page component"""
    st.markdown('<h1 class="main-header">Bookings</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Manage and view all your bookings with prediction scores.</p>', unsafe_allow_html=True)
    
    # Quick Analytics
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Cancellation Rate</h3>
            <h2 style="color: #dc2626; font-size: 2rem;">15%</h2>
            <p style="color: #dc2626;">-2%</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Booking Trend</h3>
            <h2 style="color: #059669; font-size: 2rem;">+10%</h2>
            <p style="color: #059669;">+5%</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Add New Booking button with better margins
    st.markdown('<div style="margin: 2rem 0 1rem 0;">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("+ New Booking", type="primary", use_container_width=True):
            st.session_state.page = "new_booking"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Functional filters and search bar
    st.markdown('<div style="margin: 1rem 0 2rem 0;">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        search_query = st.text_input(
            "🔍 Search bookings...",
            placeholder="Search by guest name, booking ID, or room type",
            help="Search through all bookings"
        )
    with col2:
        status_filter = st.selectbox(
            "Status",
            ["All", "Confirmed", "Cancelled"],
            help="Filter by booking status"
        )
    with col3:
        hotel_type_filter = st.selectbox(
            "Hotel Type",
            ["All", "City Hotel", "Resort Hotel"],
            help="Filter by hotel type"
        )
    with col4:
        date_filter = st.selectbox(
            "📅 Date Range",
            ["All", "This Week", "This Month", "Next Month"],
            help="Filter by date range"
        )
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<h3 style="margin-top: 2rem;">All Bookings</h3>', unsafe_allow_html=True)
    
    bookings = generate_dummy_bookings() + st.session_state.bookings
    
    # Filter bookings based on search and filters
    filtered_bookings = filter_bookings(
        bookings, 
        search_query, 
        status_filter, 
        hotel_type_filter, 
        date_filter
    )
    
    st.markdown(f'<p style="color: #6b7280; margin-bottom: 1rem;">Showing {len(filtered_bookings)} of {len(bookings)} bookings</p>', unsafe_allow_html=True)
    
    # Display table header
    st.markdown("""
    <div class="table-header">
        <div class="header-info">
            <div class="booking-id">Booking ID</div>
            <div class="guest-name">Guest Name</div>
            <div class="date">Check-in Date</div>
            <div class="date">Check-out Date</div>
            <div class="room-type">Room Type</div>
        </div>
        <div style="display: flex; gap: 20px; align-items: center;">
            <div style="min-width: 80px;">Status</div>
            <div style="min-width: 120px;">Prediction Score</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display each booking row
    for booking in filtered_bookings:
        status_class = "status-confirmed" if booking['status'] == 'Confirmed' else "status-cancelled"
        
        st.markdown(f"""
        <div class="booking-row">
            <div class="booking-info">
                <div class="booking-id">{booking['booking_id']}</div>
                <div class="guest-name">{booking['guest_name']}</div>
                <div class="date">{booking['check_in']}</div>
                <div class="date">{booking['check_out']}</div>
                <div class="room-type">{booking['hotel_type']}</div>
            </div>
            <div style="display: flex; gap: 20px; align-items: center;">
                <span class="status-badge {status_class}">{booking['status']}</span>
                <div class="prediction-container">
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {booking['prediction_score']}%"></div>
                    </div>
                    <span class="prediction-score">{booking['prediction_score']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True) 