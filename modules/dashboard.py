import streamlit as st
import pandas as pd
from utils.model import get_model_metrics

def render_dashboard():
    st.markdown("# Model Insights Dashboard")
    st.markdown("""
    <span style='color:gray'>Key metrics and insights from the cancellation prediction model.</span>
    """, unsafe_allow_html=True)
    metrics = get_model_metrics()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Accuracy", f"{metrics['Accuracy']*100:.1f}%")
    col2.metric("Precision", f"{metrics['Precision']*100:.1f}%")
    col3.metric("Recall", f"{metrics['Recall']*100:.1f}%")
    col4.metric("F1 Score", f"{metrics['F1 Score']*100:.1f}%")
    st.markdown("---")
    st.markdown("### Model Performance Over Time (Dummy)")
    st.line_chart(pd.DataFrame({
        "Accuracy": [0.82, 0.84, 0.85, 0.86, 0.87],
        "F1 Score": [0.76, 0.78, 0.79, 0.80, 0.80],
    }, index=["2024-Q1", "2024-Q2", "2024-Q3", "2025-Q1", "2025-Q2"])) 