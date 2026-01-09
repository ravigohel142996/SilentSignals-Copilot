# SilentSignals

**Detecting hidden stress before it becomes burnout.**

SilentSignals is a privacy-first Streamlit web application that helps college students recognize early stress and burnout signals by analyzing everyday behavior patterns—without asking direct mental health questions.

---

## Table of Contents

- [Overview](#overview)
- [Inspiration](#inspiration)
- [How SilentSignals Works](#how-silentsignals-works)
- [Why It's Unique](#why-its-unique)
- [Ethical and Privacy Approach](#ethical-and-privacy-approach)
- [Tech Stack](#tech-stack)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Demo Disclaimer](#demo-disclaimer)
- [Hackathon Alignment](#hackathon-alignment)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

SilentSignals detects early stress and burnout signals by analyzing everyday student behavior patterns such as:
- Sleep duration
- Screen time
- Missed deadlines
- Study workload
- Social interaction levels

The application uses transparent, rule-based logic to calculate a **Stress Signal Index** and provides supportive, non-medical guidance to help students become more aware of their patterns.

**Key Principle:** We analyze the "silent signals" in daily routines, not mental health symptoms directly. This reduces stigma and makes the tool more accessible.

---

## Inspiration

College students face immense academic and social pressure, yet many don't recognize burnout until it has already impacted their health, relationships, and performance. Traditional mental health screening can feel invasive or clinical, creating barriers for students who aren't ready for formal assessment.

**The Problem:**
- Mental health struggles often show up first in behavior changes (poor sleep, social withdrawal, missed deadlines)
- Students may not realize these patterns are stress signals
- By the time they seek help, the problem has often escalated

**Our Solution:**
- Detect stress through observable behavior patterns students are already aware of
- Provide awareness and gentle guidance, not diagnosis
- Make mental health awareness feel less clinical and more approachable
- Respect privacy completely—no data storage or tracking

---

## How SilentSignals Works

SilentSignals uses a completely transparent, rule-based approach:

### 1. Data Collection
Users provide information about their recent patterns:
- Average sleep hours per night (3-10 hours)
- Daily screen time (1-12 hours)
- Number of missed deadlines this week (0-10)
- Study workload (Low/Medium/High)
- Social interaction level (Low/Medium/High)

### 2. Stress Signal Index Calculation
The application applies straightforward, explainable rules to calculate a **Stress Signal Index** (0-100):

- **Sleep Factor (0-30 points):** Less sleep = higher stress signals
- **Screen Time Factor (0-20 points):** More screen time = higher stress signals
- **Deadline Factor (0-25 points):** More missed deadlines = higher stress signals
- **Workload Factor (0-15 points):** Higher workload = higher stress signals
- **Social Factor (0-10 points):** Less social interaction = higher stress signals

### 3. Zone Classification
The index is mapped to three zones:
- **Green Zone (0-35):** Stable - Good balance and low stress signals
- **Yellow Zone (36-65):** Rising Stress - Notable patterns worth addressing
- **Red Zone (66-100):** Burnout Risk - Multiple high-stress indicators

### 4. Explanation and Guidance
The app provides:
- Clear explanation of which factors contributed to the score
- Supportive, non-medical recommendations for small adjustments
- AI Copilot feature for deeper pattern exploration

**No Machine Learning:** All calculations follow deterministic rules that can be fully explained.

---

## Why It's Unique

### Privacy-Absolute
**Your data never leaves your browser.** SilentSignals runs entirely client-side in Streamlit. No databases, no cloud storage, no tracking, no data transmission. When you close the browser, everything is gone.

### Non-Clinical Approach
We focus on behavior patterns (sleep, workload, deadlines), not clinical symptoms (depression, anxiety). This makes the tool:
- Less intimidating for students hesitant about mental health assessment
- More accessible as a regular check-in tool
- Free from the stigma associated with clinical mental health screening

### Completely Explainable
Every score, zone, and recommendation is based on transparent, rule-based logic. No black-box algorithms or unexplainable AI. You can understand exactly why you got your score and what factors contributed.

### Student-Centered Design
Built specifically for the college experience where stress manifests through:
- Sleep disruption from studying late
- High screen time from online classes and research
- Deadline pressure from multiple courses
- Social isolation from heavy workload

### Preventive Focus
By identifying early signals, students can make small adjustments before stress escalates into crisis. The tool emphasizes awareness and prevention, not treatment.

---

## Ethical and Privacy Approach

### Privacy Commitment
- **No data collection:** We don't store, transmit, or log any user input
- **No accounts required:** Use the app anonymously
- **No tracking:** No cookies, no analytics, no user identification
- **No external APIs:** Everything runs locally in your browser

### Ethical Boundaries
SilentSignals is **NOT**:
- A diagnostic tool for mental health conditions
- A replacement for professional counseling or therapy
- Medical advice or treatment
- A validated clinical assessment

SilentSignals **IS**:
- A personal awareness tool for recognizing behavior patterns
- A non-judgmental space for reflection
- A starting point for understanding stress signals
- A gentle nudge toward self-care or seeking support if needed

### Safety and Responsibility
- Clear disclaimers throughout the app about its limitations
- Explicit guidance to seek professional help for significant distress
- Non-alarmist language that avoids creating unnecessary anxiety
- Supportive, non-judgmental tone in all recommendations

---

## Tech Stack

SilentSignals is built with simplicity and transparency in mind:

- **Python 3.8+**
- **Streamlit** - Web application framework
- **No external APIs** - Fully self-contained
- **No ML libraries** - Pure rule-based logic (no TensorFlow, scikit-learn, etc.)
- **No database** - Stateless architecture using Streamlit session state

This minimal tech stack ensures:
- Easy deployment on Streamlit Cloud
- Complete transparency in how calculations work
- Maximum privacy (no external dependencies or data transmission)
- Simple maintenance and updates

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ravigohel142996/SilentSignals-Copilot.git
   cd SilentSignals-Copilot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   The app will automatically open in your default browser, typically at `http://localhost:8501`

### Deployment on Streamlit Cloud

1. Fork or push this repository to your GitHub account
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub account
4. Select this repository
5. Set the main file path to `app.py`
6. Deploy!

The app will be live in minutes with a public URL.

---

## Usage

### Getting Started

1. **Home Page:**
   - View an overview of SilentSignals
   - See placeholder KPI metrics (until you complete an analysis)

2. **Stress Signal Analysis:**
   - Fill out the form with your recent behavior patterns
   - Click "Analyze My Stress Signals"
   - Review your Stress Signal Index, zone classification, and personalized insights
   - Read the gentle recommendations tailored to your patterns

3. **AI Copilot:**
   - Ask questions about your stress patterns
   - Get deeper explanations based on your analysis results
   - Explore "what if" scenarios and understand contributing factors

4. **About:**
   - Learn more about the project philosophy
   - Understand the privacy and ethical approach
   - Read about limitations and proper use

### Understanding Your Results

- **Stress Signal Index:** A score from 0-100 indicating the level of stress signals in your patterns (not a diagnosis)
- **Zone Classification:** Green (Stable), Yellow (Rising Stress), or Red (Burnout Risk)
- **Contributing Factors:** Specific patterns that elevated your score
- **Recommendations:** Small, actionable adjustments you might consider

---

## Demo Disclaimer

**Important:** SilentSignals is a demonstration application created for educational and awareness purposes as part of a hackathon project.

- **Not a medical device:** This is not a validated clinical tool
- **Not diagnostic:** Cannot diagnose mental health conditions
- **Not treatment:** Does not provide medical treatment or therapy
- **For awareness only:** Use for personal reflection and pattern recognition

**If you are experiencing significant distress, persistent mood changes, or thoughts of self-harm:**
- Contact campus counseling services
- Reach out to a trusted friend, family member, or mentor
- Call a mental health crisis line (988 in the US)
- Speak with a mental health professional

SilentSignals is designed to complement professional support, not replace it.

---

## Hackathon Alignment

### Snow Fest Hackathon - HealthTech Category

**Beginner-Friendly:**
- Simple, intuitive interface
- No technical jargon
- Clear instructions and explanations

**Creative & Innovative:**
- Unique approach to mental health awareness through behavior pattern analysis
- "Silent signals" concept—detecting stress without asking about mental health directly
- AI Copilot feature for interactive exploration of patterns

**HealthTech Focused:**
- Addresses student mental health and burnout prevention
- Evidence-informed approach based on known stress indicators
- Practical tool for health awareness and wellness

**Privacy-First:**
- Absolute commitment to user privacy
- No data collection or storage
- Client-side processing only

**Fully Explainable:**
- Transparent, rule-based logic (no black-box ML)
- Every calculation can be explained in plain language
- Clear cause-and-effect relationships

**Demo-Ready:**
- Complete, working application
- No placeholder code or TODOs
- Runs smoothly on Streamlit Cloud
- Professional, polished interface

**Streamlit Cloud Compatible:**
- Simple requirements (only Streamlit)
- No external API dependencies
- No database requirements
- Quick deployment process

**No External APIs:**
- Fully self-contained application
- No internet connectivity required after loading
- No third-party service dependencies

**No Machine Learning Libraries:**
- Pure rule-based logic
- No TensorFlow, PyTorch, scikit-learn, etc.
- Deterministic, explainable calculations

**No Medical Diagnosis:**
- Clear ethical boundaries
- Awareness tool, not diagnostic tool
- Supportive guidance, not medical advice

---

## Features

### Core Features
- **Stress Signal Analysis:** Rule-based calculation of stress index from behavior patterns
- **Zone Classification:** Three-tier system (Green/Yellow/Red) for easy interpretation
- **Personalized Insights:** Explanations tailored to individual patterns
- **Gentle Recommendations:** Non-medical, supportive suggestions for small adjustments
- **AI Copilot:** Interactive Q&A for deeper pattern exploration
- **KPI Dashboard:** Visual metrics showing stress level, burnout risk, and lifestyle stability

### Technical Features
- **Session State Management:** Preserves user data within a browser session
- **Responsive Design:** Wide layout for comfortable viewing
- **Form Validation:** Ensures data quality through sliders and select boxes
- **Progress Visualization:** Visual progress bars and color-coded zones
- **Multi-Page Navigation:** Clean sidebar navigation between different sections

### Privacy Features
- **No data persistence:** All data cleared when browser closes
- **No external calls:** Zero network requests after initial app load
- **No tracking:** No analytics or user identification
- **Anonymous use:** No accounts or login required

---

## Project Structure

```
SilentSignals-Copilot/
├── app.py              # Main Streamlit application (all code)
├── requirements.txt    # Python dependencies (streamlit only)
├── README.md          # This file
└── .gitignore         # Git ignore patterns
```

**Intentionally minimal:** The entire application is contained in a single `app.py` file for maximum simplicity and transparency.

---

## Contributing

This project was created for the Snow Fest Hackathon. If you'd like to extend or improve SilentSignals:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test thoroughly to ensure the app still runs correctly
5. Submit a pull request with a clear description of your changes

**Guidelines:**
- Maintain the privacy-first approach (no data collection)
- Keep the logic transparent and explainable
- Preserve the non-clinical, supportive tone
- Ensure compatibility with Streamlit Cloud
- Add clear comments for any complex logic

---

## License

This project is open source and available for educational and demonstration purposes.

**Important:** If you adapt this code for production use involving real mental health assessment:
- Consult with licensed mental health professionals
- Ensure proper validation and testing
- Consider regulatory requirements (HIPAA, etc.)
- Add appropriate clinical oversight

This demo version is designed for awareness and education, not clinical application.

---

## Acknowledgments

Created for the **Snow Fest Hackathon** with the goal of making mental health awareness more accessible and less stigmatizing for college students.

**Inspiration:**
- The silent struggles of students facing burnout
- The need for preventive tools that catch stress early
- The importance of privacy in mental health technology
- The value of transparency and explainability in health applications

**Thank you to:**
- The Snow Fest Hackathon organizers
- The Streamlit community for an amazing framework
- All students who've shared their experiences with academic stress

---

## Contact

For questions, feedback, or discussions about this project:
- GitHub Issues: [SilentSignals-Copilot Issues](https://github.com/ravigohel142996/SilentSignals-Copilot/issues)
- Project Repository: [SilentSignals-Copilot](https://github.com/ravigohel142996/SilentSignals-Copilot)

---

**Remember:** SilentSignals is here to help you notice patterns, not to judge or diagnose. You're in control of your wellbeing journey, and we're just providing information along the way.

*Explain patterns, not judge people.*
