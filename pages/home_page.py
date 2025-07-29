import streamlit as st

def home_page():
    """Home page component"""
    # Welcome message
    if st.session_state.username:
        st.markdown(f"""
        <div style="text-align: right; margin-bottom: 1rem; color: #6b7280;">
            Welcome, <strong>{st.session_state.username}</strong>! 👋
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 3rem; margin-bottom: 1rem;">Hotellingence</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.5rem; margin-bottom: 2rem;">Predict your guests\' next move</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # App Introduction
    st.markdown("""
    <div class="metric-card">
        <h2 style="text-align: center; margin-bottom: 1.5rem;">Welcome to Hotellingece</h2>
        <p style="text-align: center; font-size: 1.1rem; line-height: 1.6; color: #374151;">
            Hotellingece is an AI-powered platform designed to help hotel administrators predict booking cancellations 
            and optimize their operations. Our advanced machine learning algorithms analyze various factors including 
            hotel type, lead time, guest demographics, and booking patterns to provide accurate cancellation predictions.
        </p>
        <div style="text-align: center; margin-top: 2rem;">
            <h3 style="color: #1f2937; margin-bottom: 1rem;">Key Features:</h3>
            <ul style="text-align: left; display: inline-block; color: #374151;">
                <li>🎯 <strong>Predictive Analytics:</strong> Identify potential cancellations before they happen</li>
                <li>📊 <strong>Real-time Insights:</strong> Monitor booking trends and cancellation risks</li>
                <li>🏨 <strong>Hotel Type Analysis:</strong> Specialized predictions for City and Resort hotels</li>
                <li>👥 <strong>Guest Demographics:</strong> Consider adults, children, and babies in predictions</li>
                <li>📅 <strong>Lead Time Analysis:</strong> Factor in booking-to-arrival timing</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content - Welcome and features
    st.markdown("""
    <div class="metric-card">
        <h2 style="text-align: center; margin-bottom: 1.5rem;">How It Works</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem;">
            <div style="text-align: center; padding: 1.5rem; background-color: #f8fafc; border-radius: 8px;">
                <h3 style="color: #1f2937; margin-bottom: 1rem;">📝 1. Create Booking</h3>
                <p style="color: #6b7280;">Add new bookings with guest details, dates, and preferences</p>
            </div>
            <div style="text-align: center; padding: 1.5rem; background-color: #f8fafc; border-radius: 8px;">
                <h3 style="color: #1f2937; margin-bottom: 1rem;">🤖 2. AI Prediction</h3>
                <p style="color: #6b7280;">Our AI analyzes patterns to predict cancellation likelihood</p>
            </div>
            <div style="text-align: center; padding: 1.5rem; background-color: #f8fafc; border-radius: 8px;">
                <h3 style="color: #1f2937; margin-bottom: 1rem;">📊 3. Monitor & Manage</h3>
                <p style="color: #6b7280;">Track all bookings with real-time insights and analytics</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True) 