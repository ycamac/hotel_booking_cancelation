import streamlit as st
import plotly.express as px
import pandas as pd
import model.functions as mf


def dashboard_page():
    """Dashboard page component bound to real predictions created from New Booking."""
    st.markdown('<h1 class="main-header">Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Monitor performance and live cancellation risk from model predictions.</p>', unsafe_allow_html=True)

    bookings = st.session_state.get('bookings', [])

    # If no data yet, guide the user
    if not bookings:
        st.info("No bookings with predictions yet. Create one in New Booking to populate the dashboard.")

    df = pd.DataFrame(bookings) if bookings else pd.DataFrame(columns=[
        'booking_id', 'guest_name', 'check_in', 'check_out', 'hotel_type', 'status', 'prediction_score'
    ])

    # Key Metrics from live predictions
    total_bookings = int(len(df))
    avg_pred_risk = float(df['prediction_score'].mean()) if not df.empty else 0.0
    high_risk_count = int((df['prediction_score'] >= 70).sum()) if 'prediction_score' in df else 0
    high_risk_rate = (high_risk_count / total_bookings * 100) if total_bookings > 0 else 0.0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Bookings</h3>
            <h2 style="color: #3b82f6; font-size: 2rem;">{total_bookings}</h2>
            <p style="color: #6b7280;">in current session</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Avg Predicted Risk</h3>
            <h2 style="color: #dc2626; font-size: 2rem;">{avg_pred_risk:.1f}%</h2>
            <p style="color: #6b7280;">mean of prediction scores</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>High-Risk Bookings</h3>
            <h2 style="color: #f59e0b; font-size: 2rem;">{high_risk_count}</h2>
            <p style="color: #6b7280;">≥ 70% risk ({high_risk_rate:.0f}%)</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        metrics = mf.get_model_metrics()
        st.markdown(f"""
        <div class="metric-card">
            <h3>Model Accuracy</h3>
            <h2 style="color: #059669; font-size: 2rem;">{metrics['Accuracy']*100:.0f}%</h2>
            <p style="color: #6b7280;">static from evaluation</p>
        </div>
        """, unsafe_allow_html=True)

    # Charts
    col1, col2 = st.columns(2)
    with col1:
        # Avg predicted risk by check-in month (robust ordering and month completion)
        if not df.empty and 'check_in' in df and 'prediction_score' in df:
            parsed = pd.to_datetime(df['check_in'], errors='coerce')
            valid = pd.DataFrame({'date': parsed, 'risk': df['prediction_score']}).dropna(subset=['date'])
            if not valid.empty:
                valid['month'] = valid['date'].dt.to_period('M').dt.to_timestamp()
                trend_df = (
                    valid.groupby('month', as_index=False)['risk']
                    .mean()
                    .sort_values('month')
                )
                # Fill missing months between min and max
                start = trend_df['month'].min()
                end = trend_df['month'].max()
                full_months = pd.date_range(start=start, end=end, freq='MS')
                trend_df = (
                    trend_df.set_index('month')
                    .reindex(full_months)
                    .rename_axis('month')
                    .reset_index()
                )
            else:
                trend_df = pd.DataFrame({'month': [], 'risk': []})
        else:
            trend_df = pd.DataFrame({'month': [], 'risk': []})

        fig_trend = px.line(
            trend_df,
            x='month',
            y='risk',
            title='Avg Predicted Cancellation Risk by Month',
            labels={'month': 'Month', 'risk': 'Avg Risk (%)'}
        )
        fig_trend.update_layout(height=400)
        fig_trend.update_xaxes(dtick="M1", tickformat="%Y-%m")
        st.plotly_chart(fig_trend, use_container_width=True)

    with col2:
        # Hotel type distribution from actual bookings
        if not df.empty and 'hotel_type' in df:
            type_df = df['hotel_type'].value_counts().reset_index()
            type_df.columns = ['hotel_type', 'count']
        else:
            type_df = pd.DataFrame({'hotel_type': [], 'count': []})

        fig_types = px.pie(
            type_df,
            values='count',
            names='hotel_type',
            title='Bookings by Hotel Type'
        )
        fig_types.update_layout(height=400)
        st.plotly_chart(fig_types, use_container_width=True)

    # Recent Activity from the latest bookings
    st.markdown('<h2 style="margin-top: 3rem;">Recent Activity</h2>', unsafe_allow_html=True)

    if df.empty:
        st.markdown("""
        <div class="booking-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong>No recent activity</strong>
                    <br>
                    <small style="color: #6b7280;">Create a booking to see live updates</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        recent_df = df.tail(5).iloc[::-1]  # latest first
        for _, row in recent_df.iterrows():
            guest = row.get('guest_name', 'Guest')
            pred = row.get('prediction_score', 0)
            htype = row.get('hotel_type', '-')
            check_in = row.get('check_in', '-')
            st.markdown(f"""
            <div class="booking-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>New booking created</strong>
                        <br>
                        <small style="color: #6b7280;">{guest} • {htype} • {check_in}</small>
                    </div>
                    <div style="text-align: right;">
                        <small style="color: #6b7280;">just now</small>
                        <br>
                        <small style="color: #3b82f6;">Predicted risk: {pred:.0f}%</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)