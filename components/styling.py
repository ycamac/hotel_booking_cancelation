import streamlit as st

def load_css():
    """Load custom CSS styles"""
    st.markdown("""
    <style>

        
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1f2937;
            text-align: center ;
            margin-bottom: 0;
        }
        
        .sub-header {
            font-size: 1.2rem;
            color: #6b7280;
            text-align: center;
            margin-bottom: 3rem;
        }

        .stToastContainer{
            margin: 0 !important;
            position: 0 !important;
        }
        .stMainBlockContainer {
            padding-top: 0 !important;
            padding-bottom: 100px !important;
        }

        .stVerticalBlock {
            height: 0%;
        }
                
        /* Fix Vertical Block height inheritance */
        .stVerticalBlock {
            height: auto !important;
        }

        /* Remove unnecessary section offset */
        section.stMain {
            top: 0 !important;
        }
                
        /* Normalize stMainBlockContainer padding */
        [data-testid="stMainBlockContainer"] {
            padding-top: 0 !important;
            pointer-events: auto; /* Optional, if interaction is needed */
        }
          
        .header {
            position: fixed;
            left: 0;
            top: 0;
            padding: 5px;    
            width: 100%;
            background-color: rgb(23, 29, 59);
            color: #6b7280;
            font-family: "Work Sans", "Noto Sans", sans-serif;
            font-size: 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            padding: 5px;
            width: 100%;
            background-color: rgb(23, 29, 59);
            color: white;
            text-align: center;                
            font-size: 12px;
        }
        .button {
            background-color: rgb(255, 51, 51);
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 5px;
        }
        .metric-card {
            background-color: white;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 20px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .booking-card {
            background-color: white;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
            margin-bottom: 1rem;
        }
        
        .status-confirmed {
            background-color: #dbeafe;
            color: #1e40af;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 500;
        }
        
        .status-cancelled {
            background-color: #f3f4f6;
            color: #6b7280;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 500;
        }
        
        .prediction-score {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .progress-bar {
            flex: 1;
            height: 8px;
            background-color: #e5e7eb;
            border-radius: 4px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background-color: #3b82f6;
            border-radius: 4px;
        }
        
        .hero-section {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80');
            background-size: cover;
            background-position: center;
            padding: 12rem 2rem;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 3rem;
        }
        
        .feature-card {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            border: 1px solid #e5e7eb;
            text-align: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .team-member {
            display: flex;
            align-items: start;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .team-avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background-color: #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: #6b7280;
        }
        
        .team-info {
            flex: 1;
        }
        
        .booking-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 16px;
            border-bottom: 1px solid #e5e7eb;
            background-color: white;
        }
        .booking-info {
            display: flex;
            gap: 20px;
            align-items: center;
            flex: 1;
        }
        .booking-id {
            font-weight: 600;
            color: #1f2937;
            min-width: 100px;
        }
        .guest-name {
            color: #374151;
            min-width: 120px;
        }
        .date {
            color: #6b7280;
            min-width: 100px;
        }
        .room-type {
            color: #6b7280;
            min-width: 100px;
        }
        .status-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
            min-width: 80px;
            text-align: center;
        }
        .status-confirmed {
            background-color: #dbeafe;
            color: #1e40af;
        }
        .status-cancelled {
            background-color: #f3f4f6;
            color: #6b7280;
        }
        .prediction-container {
            display: flex;
            align-items: center;
            gap: 8px;
            min-width: 120px;
        }
        .progress-bar {
            width: 60px;
            height: 8px;
            background-color: #e5e7eb;
            border-radius: 4px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background-color: #3b82f6;
            border-radius: 4px;
        }
        .prediction-score {
            font-weight: 500;
            color: #374151;
            min-width: 30px;
        }
        .table-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 16px;
            background-color: #f8fafc;
            border-bottom: 2px solid #e5e7eb;
            font-weight: 600;
            color: #374151;
        }
        .header-info {
            display: flex;
            gap: 20px;
            align-items: center;
            flex: 1;
        }
    </style>
    """, unsafe_allow_html=True) 