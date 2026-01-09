import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(
    page_title="SilentSignals",
    layout="wide"
)

# Global CSS Design System
st.markdown("""
<style>
    /* Global Background and Color Scheme */
    .stApp {
        background-color: #F7F9FC;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #E8EDF3;
    }
    
    [data-testid="stSidebar"] .css-1d391kg {
        padding-top: 2rem;
    }
    
    /* Hide default sidebar title */
    [data-testid="stSidebar"] h1 {
        display: none;
    }
    
    /* Card Styling */
    .card {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 14px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
    }
    
    .feature-card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 14px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
        height: 100%;
    }
    
    .insight-card {
        background-color: #FFFFFF;
        padding: 2.5rem;
        border-radius: 14px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    
    .kpi-card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 14px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        text-align: center;
        height: 100%;
    }
    
    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #64748B;
        margin-bottom: 1rem;
        font-weight: 400;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: #475569;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 1rem;
        margin-top: 2rem;
    }
    
    .section-subheader {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 2rem;
    }
    
    /* Form Section Headers */
    .form-section-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1E293B;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    
    .form-section-helper {
        font-size: 0.95rem;
        color: #64748B;
        margin-bottom: 1rem;
    }
    
    /* Primary Button Styling */
    .stButton > button {
        background-color: #3B82F6;
        color: white;
        border-radius: 14px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        width: 100%;
        margin-top: 1.5rem;
    }
    
    .stButton > button:hover {
        background-color: #2563EB;
    }
    
    /* Feature Card Titles */
    .feature-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 0.75rem;
    }
    
    .feature-description {
        font-size: 1rem;
        color: #475569;
        line-height: 1.5;
    }
    
    /* KPI Styling */
    .kpi-label {
        font-size: 0.9rem;
        color: #64748B;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.25rem;
    }
    
    .kpi-delta {
        font-size: 0.9rem;
        color: #64748B;
    }
    
    /* Zone Colors */
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
    
    /* Progress Bar Styling */
    .stProgress > div > div > div > div {
        background-color: #3B82F6;
    }
    
    /* Sidebar Footer */
    .sidebar-footer {
        position: fixed;
        bottom: 1rem;
        font-size: 0.8rem;
        color: #64748B;
        padding: 0 1rem;
        line-height: 1.4;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Spacing improvements */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Form styling */
    .stForm {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 14px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    
    /* Selectbox and slider styling */
    .stSelectbox label, .stSlider label, .stNumberInput label {
        font-weight: 500;
        color: #1E293B;
    }
    
    /* Info/Warning/Success boxes */
    .stAlert {
        border-radius: 14px;
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

# Sidebar navigation with branding
st.sidebar.markdown("""
<div style="padding: 1rem 0 2rem 0;">
    <h1 style="font-size: 1.8rem; font-weight: 700; color: #1E293B; margin-bottom: 0.5rem;">SilentSignals</h1>
    <p style="font-size: 0.95rem; color: #64748B; margin: 0;">Detecting hidden stress before it becomes burnout</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Stress Signal Analysis", "AI Copilot", "About"],
    label_visibility="collapsed"
)

st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="font-size: 0.85rem; color: #64748B; line-height: 1.6; padding-top: 2rem; border-top: 1px solid #CBD5E1;">
    <strong>Privacy-first</strong> • <strong>No diagnosis</strong> • <strong>Student wellbeing</strong>
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
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">SilentSignals</h1>
        <p class="hero-subtitle">Detecting hidden stress before it becomes burnout</p>
        <p class="hero-description">
            We help students recognize early stress signals by analyzing everyday behavior patterns like sleep, screen time, and workload—without asking direct mental health questions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Cards Section
    st.markdown('<h2 class="section-header" style="text-align: center; margin-top: 3rem;">Why SilentSignals</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3 class="feature-title">Early Stress Detection</h3>
            <p class="feature-description">
                Catch stress signals before they become burnout. We analyze behavioral patterns that often change before you notice the problem yourself.
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
                Every score uses transparent, rule-based logic. No black-box algorithms—just clear cause-and-effect relationships you can understand.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI Section
    st.markdown('<h2 class="section-header" style="text-align: center; margin-top: 3rem;">Your Wellbeing Snapshot</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    if st.session_state.analysis_done:
        stress_index = st.session_state.stress_index
        zone_color, zone_label, _ = get_stress_zone(stress_index)
        
        # Calculate burnout risk level
        if stress_index <= 35:
            burnout_risk = "Low"
            risk_class = "zone-green"
        elif stress_index <= 65:
            burnout_risk = "Moderate"
            risk_class = "zone-yellow"
        else:
            burnout_risk = "High"
            risk_class = "zone-red"
        
        # Calculate lifestyle stability (inverse of stress)
        stability_score = 100 - stress_index
        
        # Get zone class for styling
        if stress_index <= 35:
            zone_class = "zone-green"
        elif stress_index <= 65:
            zone_class = "zone-yellow"
        else:
            zone_class = "zone-red"
        
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
                <div class="kpi-value {risk_class}">{burnout_risk}</div>
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
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("Navigate to 'Stress Signal Analysis' to analyze your patterns and see your personalized metrics.")

# STRESS SIGNAL ANALYSIS PAGE
elif page == "Stress Signal Analysis":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Stress Signal Analysis</h1>
        <p class="hero-subtitle">Understanding your patterns</p>
        <p class="hero-description">
            Answer a few questions about your recent patterns. This analysis uses transparent, rule-based logic to identify potential stress signals in your daily routine.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered form container
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        with st.form("stress_analysis_form"):
            # Sleep & Screen Habits Section
            st.markdown('<p class="form-section-title">Sleep & Screen Habits</p>', unsafe_allow_html=True)
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
            
            # Academic Load Section
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
            
            # Social Routine Section
            st.markdown('<p class="form-section-title">Social Routine</p>', unsafe_allow_html=True)
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
    
    # Results Section (full width)
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
        
        # Display results in insight card
        st.markdown('<div class="insight-card">', unsafe_allow_html=True)
        
        st.markdown('<h2 class="section-header" style="text-align: center;">Your Stress Signal Analysis</h2>', unsafe_allow_html=True)
        
        # Progress bar
        zone_color, zone_label, status_type = get_stress_zone(stress_index)
        
        # Center the progress bar
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.progress(stress_index / 100)
        
        # Zone indicator
        if status_type == "success":
            st.success(f"**{zone_color} Zone: {zone_label}**")
        elif status_type == "warning":
            st.warning(f"**{zone_color} Zone: {zone_label}**")
        else:
            st.error(f"**{zone_color} Zone: {zone_label}**")
        
        # Explanation
        st.markdown('<p class="section-subheader" style="margin-top: 2rem;"><strong>Understanding Your Results</strong></p>', unsafe_allow_html=True)
        explanation = get_stress_explanation(
            stress_index,
            sleep_hours,
            screen_time,
            missed_deadlines,
            workload,
            social_interaction
        )
        st.markdown(explanation)
        
        # Recommendation
        st.markdown('<p class="section-subheader" style="margin-top: 2rem;"><strong>Gentle Recommendations</strong></p>', unsafe_allow_html=True)
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
        
        st.caption("""
        **Important:** This analysis is for awareness purposes only and is not a medical diagnosis. 
        If you're experiencing significant distress, please reach out to a counselor, trusted friend, 
        or mental health professional.
        """)
    
    elif st.session_state.analysis_done:
        # Show previous results if available
        st.info("You have a previous analysis. Submit the form again to update your results.")

# AI COPILOT PAGE
elif page == "AI Copilot":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Insight Assistant</h1>
        <p class="hero-subtitle">Understanding your stress patterns</p>
        <p class="hero-description">
            Get personalized insights about your stress patterns and discover small lifestyle adjustments that might help. All responses are based on the patterns you've shared with us.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.analysis_done:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.warning("Please complete the Stress Signal Analysis first to use the Insight Assistant feature.")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Question selector in a card
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<p class="form-section-title">Ask a Question</p>', unsafe_allow_html=True)
            st.markdown('<p class="form-section-helper">Select a question to explore your stress patterns more deeply.</p>', unsafe_allow_html=True)
            
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
            
            ask_button = st.button("Get Insight", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if ask_button:
            # Response shown in insight card
            st.markdown('<div class="insight-card">', unsafe_allow_html=True)
            
            sleep = st.session_state.sleep_hours
            screen = st.session_state.screen_time
            deadlines = st.session_state.missed_deadlines
            workload = st.session_state.workload
            social = st.session_state.social_interaction
            stress_index = st.session_state.stress_index
            zone_color, zone_label, _ = get_stress_zone(stress_index)
            
            if question == "Why is my stress level rising?":
                st.markdown('<h3 class="section-header">Why is my stress level rising?</h3>', unsafe_allow_html=True)
                
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
                st.markdown('<h3 class="section-header">Which habits affect me the most?</h3>', unsafe_allow_html=True)
                
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
                st.markdown('<h3 class="section-header">What small change can help this week?</h3>', unsafe_allow_html=True)
                
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
                st.markdown('<h3 class="section-header">Is this burnout or temporary overload?</h3>', unsafe_allow_html=True)
                
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
        <p class="hero-subtitle">Understanding our approach</p>
        <p class="hero-description">
            Learn about our privacy-first philosophy, ethical boundaries, and what this tool is designed to do.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Section 1: Why SilentSignals Exists
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Why SilentSignals Exists</h2>', unsafe_allow_html=True)
    st.markdown("""
    College students face immense pressure, yet many don't recognize burnout until it's already 
    affecting their health, relationships, and academic performance. Traditional mental health 
    screening often feels invasive or clinical, creating barriers for students who aren't ready 
    to seek formal help.
    
    SilentSignals takes a different approach: we detect stress through everyday behavior patterns 
    that students are already aware of—sleep, screen time, workload, and social connection. By 
    analyzing these "silent signals," we help students recognize pressure before it becomes crisis.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 2: Privacy-First Approach
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Privacy-First Approach</h2>', unsafe_allow_html=True)
    st.markdown("""
    **Your data never leaves your browser.** SilentSignals runs entirely in your web browser using 
    Streamlit. We don't store, transmit, or share any information you enter. No databases, no 
    cloud storage, no tracking.
    
    This privacy-first design is intentional. Mental health and stress patterns are deeply personal. 
    You should be able to explore your patterns without worrying about data privacy or who might 
    see your responses.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 3: Ethical Boundaries
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">What This Tool Does NOT Do</h2>', unsafe_allow_html=True)
    st.markdown("""
    SilentSignals is **not** a diagnostic tool and does **not** provide medical advice or treatment. 
    We don't claim to diagnose depression, anxiety, burnout, or any other mental health condition.
    
    **Instead, we offer:**
    - **Awareness:** Helping you notice patterns in your lifestyle
    - **Explanation:** Showing how daily behaviors contribute to stress signals
    - **Reflection:** Creating space to think about your patterns before they become problems
    - **Guidance:** Suggesting small, non-medical adjustments that might help
    
    Think of SilentSignals as a gentle check-in system, like a friend who notices you seem tired 
    lately and suggests you might need more rest. It's information and awareness, not treatment.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 4: How It Works
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">How SilentSignals Works</h2>', unsafe_allow_html=True)
    st.markdown("""
    Our approach is completely transparent and rule-based:
    
    1. **Data Collection:** You share basic information about sleep, screen time, missed deadlines, 
       workload, and social interaction.
    
    2. **Rule-Based Analysis:** We apply straightforward, explainable rules to calculate a Stress 
       Signal Index. No machine learning, no black-box algorithms. Every calculation follows clear 
       logic that we can explain.
    
    3. **Interpretation:** We translate your index into zones (Green/Yellow/Red) and provide 
       plain-language explanations of what your patterns suggest.
    
    4. **Supportive Guidance:** We offer gentle, non-medical recommendations based on your specific 
       patterns.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 5: When to Seek Professional Help
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Built for Awareness, Not Replacement</h2>', unsafe_allow_html=True)
    st.markdown("""
    SilentSignals is designed to complement, not replace, professional support. If you're 
    experiencing significant distress, persistent mood changes, or thoughts of self-harm, please 
    reach out to:
    - Campus counseling services
    - A trusted friend or family member
    - A mental health professional
    - Crisis hotlines (988 in the US for mental health emergencies)
    
    Remember: asking for support is a strength, not a weakness.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.caption("Built with care for the Snow Fest Hackathon | HealthTech Category | 2024")
