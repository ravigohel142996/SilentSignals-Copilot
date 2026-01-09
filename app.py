import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(
    page_title="SilentSignals",
    layout="wide"
)

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

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Stress Signal Analysis", "AI Copilot", "About"]
)

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
    st.title("SilentSignals")
    st.subheader("Detecting hidden stress before it becomes burnout")
    
    st.markdown("""
    SilentSignals helps students recognize early stress and burnout signals by analyzing everyday 
    behavior patterns like sleep, screen time, and workload. We don't ask direct mental health 
    questions because sometimes the signals speak louder than words.
    
    This tool is designed to increase awareness of your lifestyle patterns, not to diagnose or 
    treat any condition. Think of it as a gentle check-in system that helps you notice patterns 
    before they become problems.
    """)
    
    st.markdown("---")
    
    # Display KPI cards
    col1, col2, col3 = st.columns(3)
    
    if st.session_state.analysis_done:
        stress_index = st.session_state.stress_index
        zone_color, zone_label, _ = get_stress_zone(stress_index)
        
        # Calculate burnout risk level
        if stress_index <= 35:
            burnout_risk = "Low"
        elif stress_index <= 65:
            burnout_risk = "Moderate"
        else:
            burnout_risk = "High"
        
        # Calculate lifestyle stability (inverse of stress)
        stability_score = 100 - stress_index
        
        with col1:
            st.metric(
                label="Stress Signal Index",
                value=f"{stress_index}/100",
                delta=zone_label
            )
        
        with col2:
            st.metric(
                label="Burnout Risk Level",
                value=burnout_risk
            )
        
        with col3:
            st.metric(
                label="Lifestyle Stability Score",
                value=f"{stability_score}/100"
            )
    else:
        with col1:
            st.metric(
                label="Stress Signal Index",
                value="--/100",
                help="Complete the Stress Signal Analysis to see your score"
            )
        
        with col2:
            st.metric(
                label="Burnout Risk Level",
                value="Not analyzed",
                help="Complete the Stress Signal Analysis to see your risk level"
            )
        
        with col3:
            st.metric(
                label="Lifestyle Stability Score",
                value="--/100",
                help="Complete the Stress Signal Analysis to see your stability score"
            )
        
        st.info("Navigate to 'Stress Signal Analysis' to analyze your patterns and see your personalized metrics.")

# STRESS SIGNAL ANALYSIS PAGE
elif page == "Stress Signal Analysis":
    st.title("Stress Signal Analysis")
    st.markdown("""
    Answer a few simple questions about your recent patterns. This analysis uses rule-based logic 
    to identify potential stress signals in your daily routine.
    """)
    
    st.markdown("---")
    
    with st.form("stress_analysis_form"):
        st.subheader("Your Recent Patterns")
        
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
        
        social_interaction = st.selectbox(
            "Social interaction level",
            options=["Low", "Medium", "High"],
            index=1,
            help="How much meaningful social interaction have you had recently?"
        )
        
        submit_button = st.form_submit_button("Analyze My Stress Signals")
    
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
        
        # Display results
        st.markdown("---")
        st.subheader("Your Stress Signal Analysis")
        
        # Progress bar
        zone_color, zone_label, status_type = get_stress_zone(stress_index)
        st.progress(stress_index / 100)
        
        # Zone indicator
        if status_type == "success":
            st.success(f"**{zone_color} Zone: {zone_label}**")
        elif status_type == "warning":
            st.warning(f"**{zone_color} Zone: {zone_label}**")
        else:
            st.error(f"**{zone_color} Zone: {zone_label}**")
        
        # Explanation
        st.markdown("### Understanding Your Results")
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
        st.markdown("### Gentle Recommendations")
        recommendation = get_recommendation(
            stress_index,
            sleep_hours,
            screen_time,
            missed_deadlines,
            workload,
            social_interaction
        )
        st.info(recommendation)
        
        st.markdown("---")
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
    st.title("SilentSignals Copilot")
    st.markdown("""
    Get personalized insights about your stress patterns and discover small lifestyle adjustments 
    that might help. All responses are based on the patterns you've shared with us.
    """)
    
    if not st.session_state.analysis_done:
        st.warning("Please complete the Stress Signal Analysis first to use the AI Copilot feature.")
    else:
        st.markdown("---")
        
        question = st.selectbox(
            "What would you like to ask?",
            options=[
                "Why is my stress level rising?",
                "Which habits affect me the most?",
                "What small change can help this week?",
                "Is this burnout or temporary overload?"
            ]
        )
        
        if st.button("Ask Copilot"):
            st.markdown("---")
            st.subheader("Copilot Response")
            
            sleep = st.session_state.sleep_hours
            screen = st.session_state.screen_time
            deadlines = st.session_state.missed_deadlines
            workload = st.session_state.workload
            social = st.session_state.social_interaction
            stress_index = st.session_state.stress_index
            zone_color, zone_label, _ = get_stress_zone(stress_index)
            
            if question == "Why is my stress level rising?":
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

# ABOUT PAGE
elif page == "About":
    st.title("About SilentSignals")
    
    st.markdown("""
    ### Why SilentSignals Exists
    
    College students face immense pressure, yet many don't recognize burnout until it's already 
    affecting their health, relationships, and academic performance. Traditional mental health 
    screening often feels invasive or clinical, creating barriers for students who aren't ready 
    to seek formal help.
    
    SilentSignals takes a different approach: we detect stress through everyday behavior patterns 
    that students are already aware of—sleep, screen time, workload, and social connection. By 
    analyzing these "silent signals," we help students recognize pressure before it becomes crisis.
    
    ### Privacy-First Approach
    
    **Your data never leaves your browser.** SilentSignals runs entirely in your web browser using 
    Streamlit. We don't store, transmit, or share any information you enter. No databases, no 
    cloud storage, no tracking.
    
    This privacy-first design is intentional. Mental health and stress patterns are deeply personal. 
    You should be able to explore your patterns without worrying about data privacy or who might 
    see your responses.
    
    ### No Diagnosis, No Treatment
    
    SilentSignals is **not** a diagnostic tool and does **not** provide medical advice or treatment. 
    We don't claim to diagnose depression, anxiety, burnout, or any other mental health condition.
    
    Instead, we offer:
    - **Awareness:** Helping you notice patterns in your lifestyle
    - **Explanation:** Showing how daily behaviors contribute to stress signals
    - **Reflection:** Creating space to think about your patterns before they become problems
    - **Guidance:** Suggesting small, non-medical adjustments that might help
    
    Think of SilentSignals as a gentle check-in system, like a friend who notices you seem tired 
    lately and suggests you might need more rest. It's information and awareness, not treatment.
    
    ### Built for Awareness, Not Replacement
    
    SilentSignals is designed to complement, not replace, professional support. If you're 
    experiencing significant distress, persistent mood changes, or thoughts of self-harm, please 
    reach out to:
    - Campus counseling services
    - A trusted friend or family member
    - A mental health professional
    - Crisis hotlines (988 in the US for mental health emergencies)
    
    ### How SilentSignals Works
    
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
    
    ### Why It's Unique
    
    **Privacy-Absolute:** No data collection, no accounts, no tracking. Your information never 
    leaves your device.
    
    **Non-Clinical:** We focus on behavior patterns, not mental health symptoms. This reduces 
    stigma and makes the tool accessible to students who aren't ready for clinical assessment.
    
    **Explainable:** Every score, zone, and recommendation is based on transparent rules. No 
    mysterious algorithms—just clear cause-and-effect relationships.
    
    **Student-Centered:** Designed specifically for the college experience, where stress often 
    manifests in academic pressure, sleep disruption, and social isolation.
    
    **Preventive:** By catching early signals, we help students make small adjustments before 
    stress becomes crisis. An ounce of prevention is worth a pound of cure.
    
    ### Tech Stack
    
    SilentSignals is built with:
    - **Streamlit:** For the interactive web interface
    - **Python:** For the rule-based logic
    - **No external APIs:** Everything runs locally in your browser
    - **No ML libraries:** Pure deterministic logic, no machine learning
    
    This simple, focused tech stack ensures reliability, transparency, and privacy.
    
    ### Demo and Hackathon Context
    
    SilentSignals was created for the **Snow Fest Hackathon** in the **HealthTech** category. 
    It demonstrates how technology can support student mental health awareness without requiring 
    medical expertise, expensive infrastructure, or invasive data collection.
    
    **Important Demo Disclaimer:** This is a demonstration application built for educational and 
    awareness purposes. While the logic is sound and the approach is evidence-informed, this is 
    not a validated clinical tool. Use it for personal reflection and awareness, not as a 
    substitute for professional assessment or care.
    
    ### Ethical Commitment
    
    We are committed to:
    - **Transparency:** All logic is explainable and non-proprietary
    - **Safety:** Clear disclaimers about the limitations of the tool
    - **Privacy:** Absolute commitment to not collecting or storing user data
    - **Responsibility:** Never claiming to diagnose or treat medical conditions
    - **Empowerment:** Helping students understand their patterns without creating anxiety
    
    ### Get Started
    
    Navigate to **Stress Signal Analysis** to begin exploring your patterns. Remember: this is 
    information for your awareness, not a diagnosis. You're in control of what you do with the 
    insights.
    
    ---
    
    **Contact & Feedback**
    
    SilentSignals is an open project created with care for student wellbeing. For questions or 
    feedback about this demo, please reach out through the project repository.
    """)
    
    st.markdown("---")
    st.caption("Built with care for the Snow Fest Hackathon | HealthTech Category | 2024")
