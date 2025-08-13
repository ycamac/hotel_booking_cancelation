import streamlit as st

def about_page():
    """About page component"""
    st.markdown('<h1 class="main-header">About Hotellingece</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Learn about our team and mission.</p>', unsafe_allow_html=True)
    
    # Company Overview
    st.markdown("""
    <div class="metric-card">
        <h2 style="text-align: center; margin-bottom: 1.5rem;">Our Mission</h2>
        <p style="text-align: center; font-size: 1.1rem; line-height: 1.6; color: #374151;">
            At Hotellingece, we believe that the future of hospitality lies in predictive intelligence. 
            Our mission is to empower hotel administrators with cutting-edge AI technology that transforms 
            how they manage bookings and predict guest behavior.
        </p>
        <p style="text-align: center; font-size: 1.1rem; line-height: 1.6; color: #374151; margin-top: 1rem;">
            By leveraging advanced machine learning algorithms, we help hotels reduce revenue loss from 
            cancellations, optimize their operations, and provide better guest experiences.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Team Section
    st.markdown('<h2 style="margin-top: 3rem;">Our Team</h2>', unsafe_allow_html=True)
    
    # Team Member 1
    st.markdown("""
    <div class="team-member">
        <div class="team-avatar">FM</div>
        <div class="team-info">
            <h3>Francisco Meza</h3>
            <p style="color: #6b7280; margin-bottom: 0.5rem;">Full Stack Developer & UI/UX Designer</p>
            <p style="color: #374151; line-height: 1.6;">
                Francisco is a skilled full stack developer with a keen eye for user experience design. 
                He focuses on creating intuitive and responsive web applications that make complex 
                data insights accessible to hotel administrators.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Team Member 2
    st.markdown("""
    <div class="team-member">
        <div class="team-avatar">YC</div>
        <div class="team-info">
            <h3>Yulian Cama</h3>
            <p style="color: #6b7280; margin-bottom: 0.5rem;">Lead Data Scientist & ML Engineer</p>
            <p style="color: #374151; line-height: 1.6;">
                Yulian is a passionate data scientist with expertise in machine learning and predictive analytics. 
                He specializes in developing AI models for the hospitality industry and has a deep understanding 
                of hotel operations and guest behavior patterns.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Values Section
    st.markdown('<h2 style="margin-top: 3rem;">Our Values</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1f2937; margin-bottom: 1rem;">🎯 Innovation</h3>
            <p style="color: #6b7280;">
                We constantly push the boundaries of what's possible with AI and machine learning 
                to deliver cutting-edge solutions for the hospitality industry.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1f2937; margin-bottom: 1rem;">🤝 Collaboration</h3>
            <p style="color: #6b7280;">
                We believe in working closely with our clients to understand their unique challenges 
                and develop tailored solutions that drive real business value.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1f2937; margin-bottom: 1rem;">📊 Excellence</h3>
            <p style="color: #6b7280;">
                We are committed to delivering the highest quality products and services, 
                ensuring that every interaction with our platform exceeds expectations.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Contact Information
    st.markdown('<h2 style="margin-top: 3rem;">Get in Touch</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="metric-card">
        <div style="text-align: center;">
            <p style="font-size: 1.1rem; color: #374151; margin-bottom: 1rem;">
                Ready to transform your hotel's booking management?
            </p>
            <p style="color: #6b7280;">
                📧 Email: info@hotellingece.com<br>
                📱 Phone: +1 (555) 123-4567<br>
                🌐 Website: www.hotellingece.com
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True) 