import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def dashboard_page():
    """Dashboard page component"""
    st.markdown('<h1 class="main-header">Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Monitor your hotel\'s performance and cancellation predictions.</p>', unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Total Bookings</h3>
            <h2 style="color: #3b82f6; font-size: 2rem;">1,234</h2>
            <p style="color: #059669;">+12% from last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Cancellation Rate</h3>
            <h2 style="color: #dc2626; font-size: 2rem;">15%</h2>
            <p style="color: #dc2626;">+2% from last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Prediction Accuracy</h3>
            <h2 style="color: #059669; font-size: 2rem;">87%</h2>
            <p style="color: #059669;">+5% from last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Revenue Impact</h3>
            <h2 style="color: #f59e0b; font-size: 2rem;">$45K</h2>
            <p style="color: #f59e0b;">Saved this month</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Cancellation trend over time - Fixed frequency issue
        # Generate monthly dates for 2024
        months = ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06',
                 '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12']
        cancellation_rates = [12, 15, 18, 14, 16, 13, 15, 17, 19, 16, 14, 15]
        
        fig = px.line(
            x=months,
            y=cancellation_rates,
            title="Cancellation Rate Trend",
            labels={'x': 'Month', 'y': 'Cancellation Rate (%)'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Hotel type distribution
        hotel_types = ['City Hotel', 'Resort Hotel']
        bookings_count = [65, 35]
        
        fig = px.pie(
            values=bookings_count,
            names=hotel_types,
            title="Bookings by Hotel Type"
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Model Performance
    st.markdown('<h2 style="margin-top: 3rem;">Model Performance</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Precision</h3>
            <h2 style="color: #059669; font-size: 2rem;">89%</h2>
            <p>Correctly identified cancellations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Recall</h3>
            <h2 style="color: #3b82f6; font-size: 2rem;">85%</h2>
            <p>Found all actual cancellations</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent Activity
    st.markdown('<h2 style="margin-top: 3rem;">Recent Activity</h2>', unsafe_allow_html=True)
    
    activities = [
        {"time": "2 hours ago", "action": "New booking created", "guest": "John Smith", "prediction": "Low risk (25%)"},
        {"time": "4 hours ago", "action": "Cancellation predicted", "guest": "Maria Garcia", "prediction": "High risk (85%)"},
        {"time": "6 hours ago", "action": "Booking confirmed", "guest": "David Wilson", "prediction": "Medium risk (45%)"},
        {"time": "1 day ago", "action": "Model retrained", "guest": "System", "prediction": "Accuracy improved to 87%"}
    ]
    
    for activity in activities:
        st.markdown(f"""
        <div class="booking-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong>{activity['action']}</strong>
                    <br>
                    <small style="color: #6b7280;">{activity['guest']}</small>
                </div>
                <div style="text-align: right;">
                    <small style="color: #6b7280;">{activity['time']}</small>
                    <br>
                    <small style="color: #3b82f6;">{activity['prediction']}</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True) 