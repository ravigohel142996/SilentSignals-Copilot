import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(
    page_title="SilentSignals",
    layout="wide"
)

# Global Premium CSS Design System
st.markdown("""
<style>
    /* Global Reset and Base */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Global Background - Soft Gray */
    .stApp {
        background-color: #F4F6FA;
    }
    
    /* Remove all Streamlit default padding/margins */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 4rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        max-width: 100% !important;
    }
    
    /* Sidebar - Product Navigation Style */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E5E7EB;
        padding: 2rem 1.5rem;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 2rem;
    }
    
    /* Sidebar Navigation Links */
    .stRadio > label {
        display: none !important;
    }
    
    .stRadio > div {
        gap: 0.5rem;
    }
    
    .stRadio > div > label {
        background-color: transparent !important;
        padding: 0.75rem 1rem !important;
        border-radius: 10px !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        color: #64748B !important;
        transition: all 0.2s ease !important;
        border: none !important;
    }
    
    .stRadio > div > label:hover {
        background-color: #F4F6FA !important;
        color: #1E293B !important;
    }
    
    .stRadio > div > label[data-baseweb="radio"] > div:first-child {
        display: none !important;
    }
    
    /* Premium Card System */
    .card {
        background-color: #FFFFFF;
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        margin-bottom: 2rem;
        border: 1px solid #F4F6FA;
    }
    
    .feature-card {
        background-color: #FFFFFF;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        margin-bottom: 1.5rem;
        height: 100%;
        border: 1px solid #F4F6FA;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    }
    
    .insight-card {
        background-color: #FFFFFF;
        padding: 3.5rem;
        border-radius: 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        margin-top: 3rem;
        margin-bottom: 3rem;
        border: 1px solid #E5E7EB;
    }
    
    .kpi-card {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        text-align: center;
        height: 100%;
        border: 1px solid #F4F6FA;
        transition: transform 0.2s ease;
    }
    
    .kpi-card:hover {
        transform: translateY(-2px);
    }
    
    /* Hero Section - Full Width Premium */
    .hero-section {
        text-align: center;
        padding: 4rem 2rem 5rem 2rem;
        margin-bottom: 3rem;
        background: linear-gradient(180deg, #FFFFFF 0%, #F4F6FA 100%);
        border-radius: 24px;
        margin-left: -3rem;
        margin-right: -3rem;
        margin-top: -3rem;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 1.25rem;
        letter-spacing: -0.02em;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 1.75rem;
        color: #64748B;
        margin-bottom: 1.5rem;
        font-weight: 400;
        letter-spacing: -0.01em;
    }
    
    .hero-description {
        font-size: 1.125rem;
        color: #475569;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* Typography System */
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 1.5rem;
        margin-top: 3rem;
        letter-spacing: -0.01em;
    }
    
    .section-subheader {
        font-size: 1.125rem;
        color: #64748B;
        margin-bottom: 2.5rem;
        line-height: 1.6;
        font-weight: 400;
    }
    
    .form-section-title {
        font-size: 1.375rem;
        font-weight: 600;
        color: #1E293B;
        margin-top: 2rem;
        margin-bottom: 0.75rem;
        letter-spacing: -0.01em;
    }
    
    .form-section-helper {
        font-size: 1rem;
        color: #64748B;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }
    
    /* Primary Button - Visually Dominant */
    .stButton > button {
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 16px !important;
        padding: 1rem 3rem !important;
        font-size: 1.125rem !important;
        font-weight: 600 !important;
        border: none !important;
        width: 100% !important;
        margin-top: 2rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
        letter-spacing: -0.01em !important;
    }
    
    .stButton > button:hover {
        background-color: #1D4ED8 !important;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.3) !important;
        transform: translateY(-1px) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
    }
    
    /* Feature Cards */
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }
    
    .feature-description {
        font-size: 1.0625rem;
        color: #475569;
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* KPI Styling */
    .kpi-label {
        font-size: 0.875rem;
        color: #64748B;
        font-weight: 500;
        margin-bottom: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .kpi-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .kpi-delta {
        font-size: 0.9375rem;
        color: #64748B;
        font-weight: 400;
    }
    
    /* Zone Colors - Softer */
    .zone-green {
        color: #10B981;
        font-weight: 600;
    }
    
    .zone-yellow {
        color: #F59E0B;
        font-weight: 600;
    }
    
    .zone-red {
        color: #EF4444;
        font-weight: 600;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-color: #2563EB !important;
        border-radius: 10px !important;
    }
    
    .stProgress > div > div {
        background-color: #E5E7EB !important;
        border-radius: 10px !important;
        height: 12px !important;
    }
    
    /* Form Elements - Premium Style */
    .stForm {
        background-color: #FFFFFF !important;
        padding: 3rem !important;
        border-radius: 20px !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
        border: 1px solid #E5E7EB !important;
    }
    
    .stSelectbox label, .stSlider label, .stNumberInput label {
        font-weight: 500 !important;
        color: #1E293B !important;
        font-size: 0.9375rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    .stSelectbox > div > div,
    .stNumberInput > div > div > input {
        border-radius: 12px !important;
        border: 1px solid #E5E7EB !important;
        font-size: 0.9375rem !important;
    }
    
    .stSlider > div > div {
        padding-top: 0.5rem !important;
    }
    
    /* Alert Boxes - Softer */
    .stAlert {
        border-radius: 16px !important;
        border: none !important;
        padding: 1.25rem 1.5rem !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
    }
    
    [data-baseweb="notification"] {
        background-color: #F0F9FF !important;
        border-left: 4px solid #2563EB !important;
    }
    
    /* Success Alert */
    .stSuccess {
        background-color: #F0FDF4 !important;
        color: #166534 !important;
        border-left: 4px solid #10B981 !important;
    }
    
    /* Warning Alert */
    .stWarning {
        background-color: #FFFBEB !important;
        color: #92400E !important;
        border-left: 4px solid #F59E0B !important;
    }
    
    /* Error Alert */
    .stError {
        background-color: #FEF2F2 !important;
        color: #991B1B !important;
        border-left: 4px solid #EF4444 !important;
    }
    
    /* Info Alert */
    .stInfo {
        background-color: #F0F9FF !important;
        color: #1E40AF !important;
        border-left: 4px solid #2563EB !important;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Caption Styling */
    .caption {
        font-size: 0.875rem;
        color: #94A3B8;
        line-height: 1.5;
        margin-top: 1rem;
    }
    
    /* Improved Spacing */
    h1, h2, h3 {
        margin-top: 0;
    }
    
    p {
        margin-bottom: 0.75rem;
    }
    
    /* Sidebar Footer */
    .sidebar-footer {
        position: fixed;
        bottom: 2rem;
        font-size: 0.8125rem;
        color: #64748B;
        line-height: 1.6;
        padding-top: 1.5rem;
        border-top: 1px solid #E5E7EB;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for storing user inputs
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False
if 'sleep_hours' not in st.session_state:
    st.session_state.sleep_hours = 7.0
if 'screen_time' not in st.session_state:
    st.session_state.screen_time = 6.0
if 'missed_deadlines' not in st.session_state:
    st.session_state.missed_deadlines = 0
if 'workload' not in st.session_state:
    st.session_state.workload = "Medium"
if 'social_interaction' not in st.session_state:
    st.session_state.social_interaction = "Medium"
if 'stress_index' not in st.session_state:
    st.session_state.stress_index = 0

# Sidebar - Premium Product Navigation
st.sidebar.markdown("""
<div style="padding: 0 0 2.5rem 0;">
    <h1 style="font-size: 1.625rem; font-weight: 700; color: #1E293B; margin-bottom: 0.5rem; letter-spacing: -0.01em;">SilentSignals</h1>
    <p style="font-size: 0.875rem; color: #64748B; margin: 0; font-weight: 400; line-height: 1.4;">Detecting hidden stress before it becomes burnout</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Stress Signal Analysis", "AI Copilot", "About"],
    label_visibility="collapsed"
)

st.sidebar.markdown("<br><br><br><br>", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="position: fixed; bottom: 2rem; width: 220px; font-size: 0.8125rem; color: #64748B; line-height: 1.6; padding-top: 1.5rem; border-top: 1px solid #E5E7EB;">
    Privacy-first • No diagnosis • Student wellbeing
</div>
""", unsafe_allow_html=True)

# Helper function to calculate stress signal index
def calculate_stress_index(sleep, screen, deadlines, workload, social):
    """
    Calculate Stress Signal Index (0-100) using rule-based logic.
    Lower scores are better (less stress).
    """
    stress_score = 0
    
    # Sleep factor (0-30 points)
    if sleep < 6:
        stress_score += 30
    elif sleep < 7:
        stress_score += 20
    elif sleep < 8:
        stress_score += 10
    else:
        stress_score += 0
    
    # Screen time factor (0-20 points)
    if screen > 10:
        stress_score += 20
    elif screen > 8:
        stress_score += 15
    elif screen > 6:
        stress_score += 10
    else:
        stress_score += 0
    
    # Missed deadlines factor (0-25 points)
    if deadlines >= 5:
        stress_score += 25
    elif deadlines >= 3:
        stress_score += 15
    elif deadlines >= 1:
        stress_score += 10
    else:
        stress_score += 0
    
    # Workload factor (0-15 points)
    if workload == "High":
        stress_score += 15
    elif workload == "Medium":
        stress_score += 8
    else:
        stress_score += 0
    
    # Social interaction factor (0-10 points)
    if social == "Low":
        stress_score += 10
    elif social == "Medium":
        stress_score += 5
    else:
        stress_score += 0
    
    return min(stress_score, 100)

def get_stress_zone(index):
    """Convert stress index to zone with color and label."""
    if index <= 35:
        return "Green", "Stable", "success"
    elif index <= 65:
        return "Yellow", "Rising Stress", "warning"
    else:
        return "Red", "Burnout Risk", "error"

def get_stress_explanation(index, sleep, screen, deadlines, workload, social):
    """Generate explanation for the stress level."""
    zone_color, zone_label, _ = get_stress_zone(index)
    
    explanation = f"Your Stress Signal Index is {index}/100, placing you in the **{zone_color} Zone ({zone_label})**.\n\n"
    
    factors = []
    
    if sleep < 7:
        factors.append(f"Your sleep duration of {sleep} hours is below the recommended 7-9 hours")
    
    if screen > 8:
        factors.append(f"Your screen time of {screen} hours per day is quite high")
    
    if deadlines >= 3:
        factors.append(f"You've missed {deadlines} deadlines this week, indicating time pressure")
    
    if workload == "High":
        factors.append("Your study workload is currently high")
    
    if social == "Low":
        factors.append("Your social interaction level is low, which can increase feelings of isolation")
    
    if factors:
        explanation += "**Contributing factors:**\n"
        for factor in factors:
            explanation += f"- {factor}\n"
    else:
        explanation += "Your lifestyle patterns show good balance across the key factors we monitor.\n"
    
    return explanation

def get_recommendation(index, sleep, screen, deadlines, workload, social):
    """Generate supportive, non-medical recommendation."""
    zone_color, zone_label, _ = get_stress_zone(index)
    
    if zone_color == "Green":
        return "Keep maintaining these healthy patterns. Your current routine shows good balance and stability."
    elif zone_color == "Yellow":
        recommendations = []
        
        if sleep < 7:
            recommendations.append("Consider adjusting your sleep schedule to get closer to 8 hours per night")
        
        if screen > 8:
            recommendations.append("Try reducing screen time by taking short breaks every hour")
        
        if deadlines >= 1:
            recommendations.append("Breaking larger tasks into smaller, manageable steps might help with deadline management")
        
        if social == "Low":
            recommendations.append("Even brief social connections, like a coffee chat or study group, can provide helpful balance")
        
        if recommendations:
            return "These signals suggest increased pressure. Consider small adjustments:\n\n" + "\n".join(f"- {rec}" for rec in recommendations)
        else:
            return "Your patterns show some stress signals. Focus on maintaining consistency in your daily routines."
    else:
        return "These patterns suggest significant pressure. Consider reaching out to your support network, talking to friends, or connecting with campus resources. Remember, asking for support is a strength, not a weakness."

# HOME PAGE
if page == "Home":
    # Hero Section - Full Width
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">SilentSignals</h1>
        <p class="hero-subtitle">Detecting hidden stress before it becomes burnout</p>
        <p class="hero-description">
            A premium wellbeing platform that helps you recognize early stress signals through everyday patterns—no direct mental health questions, complete privacy.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Cards Section - Large & Prominent
    st.markdown('<h2 class="section-header" style="text-align: center; margin-top: 4rem; margin-bottom: 2.5rem;">Why SilentSignals</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3 class="feature-title">Early Stress Signals</h3>
            <p class="feature-description">
                Catch stress before it becomes burnout. Our platform analyzes behavioral patterns that change before you notice the problem, giving you time to adjust.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3 class="feature-title">Privacy-First Design</h3>
            <p class="feature-description">
                Your data never leaves your browser. No accounts, no tracking, no storage. Complete anonymity and privacy in your wellbeing journey.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3 class="feature-title">Explainable Insights</h3>
            <p class="feature-description">
                Every score uses transparent logic. No algorithms you can't understand—just clear cause-and-effect relationships.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Insight Cards Section
    st.markdown('<h2 class="section-header" style="text-align: center; margin-top: 4rem; margin-bottom: 2.5rem;">Your Wellbeing Snapshot</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    if st.session_state.analysis_done:
        stress_index = st.session_state.stress_index
        zone_color, zone_label, _ = get_stress_zone(stress_index)
        
        # Calculate burnout risk level and get zone class for styling
        if stress_index <= 35:
            burnout_risk = "Low"
            zone_class = "zone-green"
        elif stress_index <= 65:
            burnout_risk = "Moderate"
            zone_class = "zone-yellow"
        else:
            burnout_risk = "High"
            zone_class = "zone-red"
        
        # Calculate lifestyle stability (inverse of stress)
        stability_score = 100 - stress_index
        
        with col1:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">Stress Signal Index</div>
                <div class="kpi-value">{stress_index}/100</div>
                <div class="kpi-delta {zone_class}">{zone_label}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">Burnout Risk Level</div>
                <div class="kpi-value {zone_class}">{burnout_risk}</div>
                <div class="kpi-delta">Based on current patterns</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">Lifestyle Stability Score</div>
                <div class="kpi-value">{stability_score}/100</div>
                <div class="kpi-delta">Overall balance indicator</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        with col1:
            st.markdown("""
            <div class="kpi-card">
                <div class="kpi-label">Stress Signal Index</div>
                <div class="kpi-value">--/100</div>
                <div class="kpi-delta">Complete analysis to see</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="kpi-card">
                <div class="kpi-label">Burnout Risk Level</div>
                <div class="kpi-value">Not analyzed</div>
                <div class="kpi-delta">Complete analysis to see</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="kpi-card">
                <div class="kpi-label">Lifestyle Stability Score</div>
                <div class="kpi-value">--/100</div>
                <div class="kpi-delta">Complete analysis to see</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="text-align: center; padding: 2.5rem;">
            <p style="font-size: 1.125rem; color: #64748B; margin: 0;">
                Navigate to <strong style="color: #2563EB;">Stress Signal Analysis</strong> to analyze your patterns and see your personalized metrics.
            </p>
        </div>
        """, unsafe_allow_html=True)

# STRESS SIGNAL ANALYSIS PAGE
elif page == "Stress Signal Analysis":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Stress Signal Analysis</h1>
        <p class="hero-subtitle">Understanding your patterns</p>
        <p class="hero-description">
            Share your recent patterns with us. Our transparent analysis identifies potential stress signals in your daily routine.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered Premium Form Container
    col_left, col_center, col_right = st.columns([1, 2.5, 1], gap="large")
    
    with col_center:
        st.markdown('<div class="card" style="padding: 3.5rem;">', unsafe_allow_html=True)
        
        with st.form("stress_analysis_form"):
            # Section 1: Sleep & Digital Habits
            st.markdown('<p class="form-section-title">Sleep & Digital Habits</p>', unsafe_allow_html=True)
            st.markdown('<p class="form-section-helper">How are your rest and digital engagement patterns?</p>', unsafe_allow_html=True)
            
            sleep_hours = st.slider(
                "Average sleep hours per night",
                min_value=3.0,
                max_value=10.0,
                value=7.0,
                step=0.5,
                help="How many hours do you typically sleep each night?"
            )
            
            screen_time = st.slider(
                "Daily screen time (hours)",
                min_value=1.0,
                max_value=12.0,
                value=6.0,
                step=0.5,
                help="Total hours spent on screens including study, social media, and entertainment"
            )
            
            # Section 2: Academic Load
            st.markdown('<p class="form-section-title">Academic Load</p>', unsafe_allow_html=True)
            st.markdown('<p class="form-section-helper">How are you managing your workload and deadlines?</p>', unsafe_allow_html=True)
            
            missed_deadlines = st.number_input(
                "Missed deadlines this week",
                min_value=0,
                max_value=10,
                value=0,
                step=1,
                help="How many deadlines or commitments did you miss this week?"
            )
            
            workload = st.selectbox(
                "Study workload",
                options=["Low", "Medium", "High"],
                index=1,
                help="How would you describe your current academic workload?"
            )
            
            # Section 3: Social Balance
            st.markdown('<p class="form-section-title">Social Balance</p>', unsafe_allow_html=True)
            st.markdown('<p class="form-section-helper">How connected do you feel with others?</p>', unsafe_allow_html=True)
            
            social_interaction = st.selectbox(
                "Social interaction level",
                options=["Low", "Medium", "High"],
                index=1,
                help="How much meaningful social interaction have you had recently?"
            )
            
            # Primary CTA Button
            submit_button = st.form_submit_button("Analyze Stress Signals")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Results Section - Full Width Insight Panel
    if submit_button:
        # Store values in session state
        st.session_state.sleep_hours = sleep_hours
        st.session_state.screen_time = screen_time
        st.session_state.missed_deadlines = missed_deadlines
        st.session_state.workload = workload
        st.session_state.social_interaction = social_interaction
        st.session_state.analysis_done = True
        
        # Calculate stress index
        stress_index = calculate_stress_index(
            sleep_hours,
            screen_time,
            missed_deadlines,
            workload,
            social_interaction
        )
        st.session_state.stress_index = stress_index
        
        # WOW Insight Panel - Premium Results Display
        st.markdown('<div class="insight-card">', unsafe_allow_html=True)
        
        st.markdown('<h2 class="section-header" style="text-align: center; margin-top: 0;">Your Stress Signal Report</h2>', unsafe_allow_html=True)
        st.markdown('<p class="section-subheader" style="text-align: center;">A calm, professional insight into your patterns</p>', unsafe_allow_html=True)
        
        # Progress bar - Large stress index bar
        zone_color, zone_label, status_type = get_stress_zone(stress_index)
        
        st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
        col_empty1, col_prog, col_empty2 = st.columns([1, 3, 1])
        with col_prog:
            st.markdown(f'<p style="text-align: center; font-size: 1.125rem; color: #64748B; margin-bottom: 0.75rem;">Stress Signal Index: <strong style="color: #1E293B; font-size: 1.5rem;">{stress_index}/100</strong></p>', unsafe_allow_html=True)
            st.progress(stress_index / 100)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Big risk label
        col_empty1, col_zone, col_empty2 = st.columns([1, 2, 1])
        with col_zone:
            if status_type == "success":
                st.success(f"**{zone_label}** — Your patterns show good balance")
            elif status_type == "warning":
                st.warning(f"**{zone_label}** — Some patterns worth addressing")
            else:
                st.error(f"**{zone_label}** — Multiple stress indicators detected")
        
        # Consultant-style explanation
        st.markdown('<div style="margin-top: 3rem;">', unsafe_allow_html=True)
        st.markdown('<p class="section-subheader" style="margin-bottom: 1rem;"><strong>Understanding Your Results</strong></p>', unsafe_allow_html=True)
        explanation = get_stress_explanation(
            stress_index,
            sleep_hours,
            screen_time,
            missed_deadlines,
            workload,
            social_interaction
        )
        st.markdown(explanation)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Recommendation in softer tone
        st.markdown('<div style="margin-top: 2rem; background-color: #F0F9FF; padding: 2rem; border-radius: 16px; border-left: 4px solid #2563EB;">', unsafe_allow_html=True)
        st.markdown('<p class="section-subheader" style="margin-bottom: 1rem; margin-top: 0;"><strong>Supportive Guidance</strong></p>', unsafe_allow_html=True)
        recommendation = get_recommendation(
            stress_index,
            sleep_hours,
            screen_time,
            missed_deadlines,
            workload,
            social_interaction
        )
        st.info(recommendation)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <p class="caption" style="text-align: center; margin-top: 2rem; color: #94A3B8;">
            This analysis is for awareness purposes only and is not a medical diagnosis. 
            If you're experiencing significant distress, please reach out to a counselor or mental health professional.
        </p>
        """, unsafe_allow_html=True)
    
    elif st.session_state.analysis_done:
        # Show previous results if available
        st.markdown("""
        <div class="card" style="text-align: center; padding: 2.5rem; margin-top: 2rem;">
            <p style="font-size: 1.125rem; color: #64748B; margin: 0;">
                You have a previous analysis. <strong style="color: #2563EB;">Submit the form again</strong> to update your results.
            </p>
        </div>
        """, unsafe_allow_html=True)

# AI COPILOT PAGE
elif page == "AI Copilot":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Insight Consultant</h1>
        <p class="hero-subtitle">Your personal stress pattern advisor</p>
        <p class="hero-description">
            Explore your stress patterns with our consultant view. Get professional insights and discover small lifestyle adjustments tailored to your unique situation.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.analysis_done:
        st.markdown('<div class="card" style="text-align: center; padding: 3rem;">', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.125rem; color: #64748B; margin: 0;">
            Please complete the <strong style="color: #2563EB;">Stress Signal Analysis</strong> first to access personalized insights.
        </p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Consultant Panel - Question selector
        col_left, col_center, col_right = st.columns([1, 2.5, 1], gap="large")
        
        with col_center:
            st.markdown('<div class="card" style="padding: 3rem;">', unsafe_allow_html=True)
            st.markdown('<p class="form-section-title" style="margin-top: 0; text-align: center;">Select Your Question</p>', unsafe_allow_html=True)
            st.markdown('<p class="form-section-helper" style="text-align: center;">Choose a topic to explore your stress patterns more deeply</p>', unsafe_allow_html=True)
            
            question = st.selectbox(
                "Choose your question:",
                options=[
                    "Why is my stress level rising?",
                    "Which habits affect me the most?",
                    "What small change can help this week?",
                    "Is this burnout or temporary overload?"
                ],
                label_visibility="collapsed"
            )
            
            ask_button = st.button("Get Professional Insight", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if ask_button:
            # Advisory Note Style - Structured Explanation Block
            st.markdown('<div class="insight-card">', unsafe_allow_html=True)
            
            sleep = st.session_state.sleep_hours
            screen = st.session_state.screen_time
            deadlines = st.session_state.missed_deadlines
            workload = st.session_state.workload
            social = st.session_state.social_interaction
            stress_index = st.session_state.stress_index
            zone_color, zone_label, _ = get_stress_zone(stress_index)
            
            if question == "Why is my stress level rising?":
                st.markdown('<h3 class="section-header" style="margin-top: 0;">Why Your Stress Level Is Rising</h3>', unsafe_allow_html=True)
                st.markdown('<p style="font-size: 1rem; color: #94A3B8; margin-bottom: 2rem;">Professional assessment based on your patterns</p>', unsafe_allow_html=True)
                
                response = f"""Based on your recent sleep and workload patterns, here's what the signals suggest:

Your Stress Signal Index of {stress_index}/100 reflects a combination of factors in your daily routine. """
                
                key_factors = []
                if sleep < 7:
                    key_factors.append(f"Sleep duration ({sleep} hours) is below optimal levels, which can affect recovery and resilience")
                if screen > 8:
                    key_factors.append(f"Extended screen time ({screen} hours) may be contributing to mental fatigue")
                if deadlines >= 1:
                    key_factors.append(f"Time pressure from {deadlines} missed deadline(s) can create a cascade of stress")
                if workload == "High":
                    key_factors.append("High academic workload is naturally demanding on your energy and time")
                if social == "Low":
                    key_factors.append("Limited social connection may reduce your support outlets")
                
                if key_factors:
                    response += "The main contributors appear to be:\n\n"
                    for factor in key_factors:
                        response += f"- {factor}\n"
                    response += "\nThese signals suggest increased pressure, not a diagnosis. They're patterns worth noticing."
                else:
                    response += "Interestingly, your individual factors look relatively balanced. Sometimes stress rises from combinations that are harder to pinpoint, or from factors outside these basic patterns."
                
                st.info(response)
            
            elif question == "Which habits affect me the most?":
                st.markdown('<h3 class="section-header" style="margin-top: 0;">Your Most Impactful Habits</h3>', unsafe_allow_html=True)
                st.markdown('<p style="font-size: 1rem; color: #94A3B8; margin-bottom: 2rem;">Prioritized analysis of contributing factors</p>', unsafe_allow_html=True)
                
                response = "Let me break down which patterns are contributing most to your current stress signals:\n\n"
                
                factors_with_impact = []
                
                if sleep < 6:
                    factors_with_impact.append(("Sleep", "High impact", f"At {sleep} hours, this is significantly below optimal levels"))
                elif sleep < 7:
                    factors_with_impact.append(("Sleep", "Moderate impact", f"At {sleep} hours, you could benefit from a bit more rest"))
                
                if screen > 10:
                    factors_with_impact.append(("Screen time", "High impact", f"{screen} hours is quite high and may be affecting your mental energy"))
                elif screen > 8:
                    factors_with_impact.append(("Screen time", "Moderate impact", f"{screen} hours could be reduced for better balance"))
                
                if deadlines >= 5:
                    factors_with_impact.append(("Deadline management", "High impact", f"{deadlines} missed deadlines suggests significant time pressure"))
                elif deadlines >= 3:
                    factors_with_impact.append(("Deadline management", "Moderate impact", f"{deadlines} missed deadlines indicates some time management challenges"))
                elif deadlines >= 1:
                    factors_with_impact.append(("Deadline management", "Minor impact", "A few missed deadlines are common but worth addressing"))
                
                if workload == "High":
                    factors_with_impact.append(("Workload", "Moderate impact", "High workload naturally creates pressure"))
                
                if social == "Low":
                    factors_with_impact.append(("Social connection", "Moderate impact", "Low social interaction reduces emotional support outlets"))
                
                if factors_with_impact:
                    for habit, impact, explanation in factors_with_impact:
                        response += f"**{habit}** ({impact}): {explanation}\n\n"
                    
                    response += "Focus on the high-impact areas first for the most noticeable improvement in your overall stress signals."
                else:
                    response += "Your patterns are quite balanced across the board. No single habit stands out as a major contributor. This is actually a good sign of lifestyle stability."
                
                st.info(response)
            
            elif question == "What small change can help this week?":
                st.markdown('<h3 class="section-header" style="margin-top: 0;">Recommended Action This Week</h3>', unsafe_allow_html=True)
                st.markdown('<p style="font-size: 1rem; color: #94A3B8; margin-bottom: 2rem;">One actionable step tailored to your situation</p>', unsafe_allow_html=True)
                
                response = "Based on your specific patterns, here's one small, actionable change you could try this week:\n\n"
                
                # Prioritize recommendations
                if sleep < 7:
                    response += """**Sleep Priority: Add 30 minutes to your sleep schedule**

Try moving your bedtime 30 minutes earlier this week. Even this small adjustment can improve recovery and resilience. Start with just one or two nights to make it manageable.

Why this helps: Sleep is foundational to managing stress. With your current pattern of {0} hours, even a modest increase can make a noticeable difference in how you handle daily pressures.""".format(sleep)
                
                elif deadlines >= 3:
                    response += f"""**Time Management: The 10-minute rule**

When you get a new task or deadline, spend just 10 minutes breaking it into smaller steps and estimating time needed. This simple habit can prevent the overwhelm that leads to missed deadlines.

Why this helps: With {deadlines} missed deadlines this week, the issue likely isn't ability but planning. Small upfront planning creates big downstream relief."""
                
                elif screen > 8:
                    response += f"""**Screen Break: The 20-20-20 rule**

Every 20 minutes of screen time, look at something 20 feet away for 20 seconds. Set a timer if needed. This reduces mental fatigue from your current {screen} hours of daily screen time.

Why this helps: High screen time isn't just about the hours—it's about continuous mental engagement without breaks. Small pauses can restore focus and reduce strain."""
                
                elif social == "Low":
                    response += """**Connection: One 15-minute conversation**

Schedule one brief, real conversation this week—coffee, a walk, or even a phone call. Not a text thread, but actual talking.

Why this helps: Low social interaction can amplify stress because we lose perspective and support. Even small connections can provide unexpected relief and remind you you're not alone in the pressure."""
                
                elif workload == "High":
                    response += """**Workload Management: The priority matrix**

List everything on your plate and mark each as either "urgent" or "can wait." Focus only on the truly urgent items this week and let the rest sit without guilt.

Why this helps: High workload feels overwhelming when everything seems equally important. Distinguishing actual urgency reduces mental load even if the tasks remain."""
                
                else:
                    response += """**Maintenance: The daily check-in**

Since your patterns are relatively balanced, focus on maintaining consistency. Take 2 minutes each evening to notice: How did today feel? What went well? What was hard?

Why this helps: When things are stable, the key is noticing small shifts before they become patterns. This brief reflection builds awareness."""
                
                st.success(response)
            
            elif question == "Is this burnout or temporary overload?":
                st.markdown('<h3 class="section-header" style="margin-top: 0;">Burnout vs. Temporary Overload</h3>', unsafe_allow_html=True)
                st.markdown('<p style="font-size: 1rem; color: #94A3B8; margin-bottom: 2rem;">Professional perspective on your current state</p>', unsafe_allow_html=True)
                
                response = f"""Let me help you understand what your patterns suggest:

Your Stress Signal Index is {stress_index}/100, which places you in the **{zone_color} Zone ({zone_label})**. """
                
                if stress_index <= 35:
                    response += """

**Assessment: Temporary pressures, not burnout**

Your patterns show normal academic stress but don't indicate burnout. You're managing relatively well, and the pressures you're feeling appear temporary and situational rather than chronic.

**Key distinction:** Temporary overload usually involves specific stressors (like exam week) while maintaining relatively healthy patterns. Burnout involves a deeper depletion where even previously manageable tasks feel impossible.

Your current patterns suggest you have good foundations in place. Keep monitoring for changes, but this appears to be normal student life pressure."""
                
                elif stress_index <= 65:
                    response += """

**Assessment: Elevated stress with some warning signs**

Your patterns show more than temporary overload but aren't yet at full burnout. Think of this as the yellow warning light—it's alerting you before things become critical.

**Key indicators:** """
                    
                    if sleep < 6:
                        response += "Poor sleep recovery patterns. "
                    if deadlines >= 3:
                        response += "Consistent time pressure and deadline struggles. "
                    if workload == "High" and social == "Low":
                        response += "High demands with low support outlets. "
                    
                    response += """

**What this means:** You're in the zone where small changes can prevent progression toward burnout. This isn't a diagnosis—it's a signal to pay attention and make some adjustments. The good news is you're catching it early enough that modest changes can make a real difference.

Consider this a reminder to prioritize recovery and balance before the pressure intensifies."""
                
                else:
                    response += """

**Assessment: Significant pressure with burnout risk signals**

Your patterns show multiple indicators of sustained high stress. This goes beyond temporary overload and suggests deeper depletion of your resilience and resources.

**Important context:** This isn't a diagnosis, but these patterns—"""
                    
                    factors = []
                    if sleep < 6:
                        factors.append("chronic sleep deprivation")
                    if screen > 10:
                        factors.append("very high screen demands")
                    if deadlines >= 5:
                        factors.append("persistent time pressure")
                    if workload == "High":
                        factors.append("heavy workload")
                    if social == "Low":
                        factors.append("low social support")
                    
                    if factors:
                        response += ", ".join(factors)
                    
                    response += """—are associated with burnout risk rather than simple temporary overload.

**What to do:** This is a good time to reach out for support. Talk to friends, family, an academic advisor, or a counselor. You don't have to manage this level of pressure alone, and asking for help is a sign of good judgment, not weakness.

Remember: These signals don't define you. They're information that can help you make informed decisions about seeking support and adjusting your load."""
                
                st.warning(response) if stress_index > 65 else st.info(response)
            
            st.markdown('</div>', unsafe_allow_html=True)

# ABOUT PAGE
elif page == "About":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">About SilentSignals</h1>
        <p class="hero-subtitle">Building trust through transparency</p>
        <p class="hero-description">
            Learn about our approach, values, and ethical boundaries. Understanding how we work is part of our commitment to you.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cards with clear visual hierarchy
    col_left, col_center, col_right = st.columns([0.5, 3, 0.5])
    
    with col_center:
        # Section 1: Purpose
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header" style="margin-top: 0;">Our Purpose</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8;">
        College students face immense pressure, yet many don't recognize burnout until it affects their health and performance. Traditional mental health screening can feel invasive, creating barriers for students who aren't ready for formal assessment.
        </p>
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8; margin-top: 1.5rem;">
        SilentSignals takes a different approach: we detect stress through everyday behavior patterns that you're already aware of—sleep, screen time, workload, and social connection. By analyzing these silent signals, we help you recognize pressure before it becomes crisis.
        </p>
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Section 2: Privacy
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header" style="margin-top: 0;">Privacy-First Philosophy</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8;">
        <strong style="color: #1E293B;">Your data never leaves your browser.</strong> SilentSignals runs entirely in your web browser. We don't store, transmit, or share any information you enter. No databases, no cloud storage, no tracking.
        </p>
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8; margin-top: 1.5rem;">
        This privacy-first design is intentional. Mental health patterns are deeply personal. You should be able to explore your wellbeing without worrying about data privacy or who might see your information.
        </p>
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Section 3: Boundaries
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header" style="margin-top: 0;">What We Don\'t Do</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8;">
        SilentSignals is <strong style="color: #1E293B;">not a diagnostic tool</strong> and does <strong style="color: #1E293B;">not provide medical advice</strong>. We don't diagnose depression, anxiety, burnout, or any mental health condition.
        </p>
        <div style="background-color: #F4F6FA; padding: 2rem; border-radius: 16px; margin-top: 2rem;">
            <p style="font-size: 1rem; color: #1E293B; font-weight: 600; margin-bottom: 1rem;">Instead, we offer:</p>
            <ul style="font-size: 1.0625rem; color: #475569; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.75rem;"><strong>Awareness</strong> — Helping you notice patterns in your lifestyle</li>
                <li style="margin-bottom: 0.75rem;"><strong>Explanation</strong> — Showing how behaviors contribute to stress signals</li>
                <li style="margin-bottom: 0.75rem;"><strong>Reflection</strong> — Creating space to think about patterns</li>
                <li><strong>Guidance</strong> — Suggesting small, non-medical adjustments</li>
            </ul>
        </div>
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8; margin-top: 2rem;">
        Think of SilentSignals as a gentle check-in system—information and awareness, not treatment.
        </p>
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Section 4: How It Works
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header" style="margin-top: 0;">How It Works</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8;">
        Our approach is completely transparent and rule-based. No machine learning, no black-box algorithms. Every calculation follows clear logic that we can explain.
        </p>
        <div style="margin-top: 2rem;">
            <div style="background-color: #F4F6FA; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;">
                <p style="font-size: 1rem; color: #1E293B; font-weight: 600; margin: 0;">1. Data Collection</p>
                <p style="font-size: 0.9375rem; color: #64748B; margin: 0.5rem 0 0 0;">Share basic information about sleep, screen time, workload, and social patterns</p>
            </div>
            <div style="background-color: #F4F6FA; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;">
                <p style="font-size: 1rem; color: #1E293B; font-weight: 600; margin: 0;">2. Rule-Based Analysis</p>
                <p style="font-size: 0.9375rem; color: #64748B; margin: 0.5rem 0 0 0;">Apply straightforward rules to calculate your Stress Signal Index</p>
            </div>
            <div style="background-color: #F4F6FA; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;">
                <p style="font-size: 1rem; color: #1E293B; font-weight: 600; margin: 0;">3. Clear Interpretation</p>
                <p style="font-size: 0.9375rem; color: #64748B; margin: 0.5rem 0 0 0;">Translate your index into zones with plain-language explanations</p>
            </div>
            <div style="background-color: #F4F6FA; padding: 1.5rem; border-radius: 12px;">
                <p style="font-size: 1rem; color: #1E293B; font-weight: 600; margin: 0;">4. Supportive Guidance</p>
                <p style="font-size: 0.9375rem; color: #64748B; margin: 0.5rem 0 0 0;">Offer gentle, non-medical recommendations based on your patterns</p>
            </div>
        </div>
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Section 5: When to Seek Help
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header" style="margin-top: 0;">When to Seek Professional Support</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8;">
        SilentSignals complements professional support—it doesn't replace it. If you're experiencing significant distress, persistent mood changes, or thoughts of self-harm, please reach out to:
        </p>
        <div style="background-color: #FEF2F2; padding: 2rem; border-radius: 16px; margin-top: 2rem; border-left: 4px solid #EF4444;">
            <ul style="font-size: 1.0625rem; color: #475569; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
                <li style="margin-bottom: 0.75rem;">Campus counseling services</li>
                <li style="margin-bottom: 0.75rem;">A trusted friend or family member</li>
                <li style="margin-bottom: 0.75rem;">A mental health professional</li>
                <li>Crisis hotlines (988 in the US)</li>
            </ul>
        </div>
        <p style="font-size: 1.0625rem; color: #475569; line-height: 1.8; margin-top: 2rem;">
        <strong style="color: #1E293B;">Remember:</strong> Asking for support is a strength, not a weakness.
        </p>
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <p class="caption" style="text-align: center; color: #94A3B8;">
        Built with care for the Snow Fest Hackathon • HealthTech Category • 2024
    </p>
    """, unsafe_allow_html=True)
