
import streamlit as st
import pandas as pd

st.set_page_config(page_title="StratAI Interactive Demo", layout="wide")
st.title("StratAI Interactive Demo")
st.subheader("AI Solutions by StratDesign Solutions")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Higher Ed: Retention & Advising",
    "Higher Ed: Advisor Matching",
    "K–12: Early Warning, Tutoring, Admin Assist",
    "Higher Ed: Curriculum & Research Tools",
    "Admin & Faculty Automations",
    "Cross-Sector & Global Solutions"
])

st.markdown("Note: This is a functional mockup interface. Data loading occurs in live deployment.")

with tab1:
    st.header("Retention & Enrollment Forecasting")
    st.write("Explore student-level retention risks and suggested interventions.")

with tab2:
    st.header("Smart Advisor Matching")
    st.write("AI-generated advisor matches based on profile compatibility.")

with tab3:
    st.header("K–12 Early Warning Dashboard")
    st.write("Monitor attendance, behavior, and academics to flag students needing support.")
    st.header("Career Readiness Alignment (Grades 6–12)")
    st.write("Explore student pathways based on interest clusters and readiness scores.")
    st.header("AI-Powered Tutoring Assistant")
    st.write("Identifies at-risk learners and recommends adaptive tutoring and resources.")
    st.header("K–12 Admin Assistant")
    st.write("Automates attendance alerts, parent communications, and IEP summaries.")

with tab4:
    st.header("Curriculum Mapping Tool")
    st.write("Align courses with learning outcomes and future workforce needs.")
    st.header("AI-Powered Research & Evaluation Tools")
    st.write("Helps faculty and institutions evaluate program success and research impact.")

with tab5:
    st.header("Admin & Faculty Task Automations")
    st.write("Automates reports, emails, meeting summaries, and Q&A for faculty/admin.")

with tab6:
    st.header("Cross-Sector & Global Solutions")
    st.write("Supports government, health, nonprofit, mining/oil, and Global South development efforts.")

st.markdown("---")
st.markdown("Powered by **StratDesign Solutions** | [Schedule a Demo](https://www.stratdesignsolutions.com/contact)")



# --- Construction ---
def calculate_construction_score(row):
    score = (
        row['cost_alert_system'] * 0.35 +
        row['safety_compliance_tracking'] * 0.35 +
        row['equipment_uptime_analytics'] * 0.30
    )
    if score >= 80:
        status = "Tech-Driven"
    elif score >= 50:
        status = "Partially Automated"
    else:
        status = "Manual Ops"
    return round(score, 2), status

def construction_dashboard():
    st.title("🏗️ Construction")
    df = pd.read_csv("Construction_Score_Mock.csv")
    scores, statuses = [], []
    for _, row in df.iterrows():
        score, status = calculate_construction_score(row)
        scores.append(score)
        statuses.append(status)
    df['Score'] = scores
    df['Status'] = statuses
    st.dataframe(df)
    st.bar_chart(df['Status'].value_counts())
    st.download_button("📥 Download Results", df.to_csv(index=False), file_name="construction_scores.csv")

# --- Transportation ---
def calculate_transportation_score(row):
    score = (
        row['route_optimization'] * 0.4 +
        row['fleet_forecasting'] * 0.3 +
        row['mobility_planning'] * 0.3
    )
    if score >= 80:
        status = "Smart Transport"
    elif score >= 50:
        status = "Growing Network"
    else:
        status = "Conventional Fleet"
    return round(score, 2), status

def transportation_dashboard():
    st.title("🚚 Transportation")
    df = pd.read_csv("Transportation_Score_Mock.csv")
    scores, statuses = [], []
    for _, row in df.iterrows():
        score, status = calculate_transportation_score(row)
        scores.append(score)
        statuses.append(status)
    df['Score'] = scores
    df['Status'] = statuses
    st.dataframe(df)
    st.bar_chart(df['Status'].value_counts())
    st.download_button("📥 Download Results", df.to_csv(index=False), file_name="transportation_scores.csv")

# --- Retail ---
def calculate_retail_score(row):
    score = (
        row['dynamic_pricing'] * 0.4 +
        row['churn_prediction_accuracy'] * 0.3 +
        row['inventory_ai_score'] * 0.3
    )
    if score >= 80:
        status = "AI Retail Leader"
    elif score >= 50:
        status = "Moderate Innovation"
    else:
        status = "Legacy Retail"
    return round(score, 2), status

def retail_dashboard():
    st.title("🛍️ Retail")
    df = pd.read_csv("Retail_Score_Mock.csv")
    scores, statuses = [], []
    for _, row in df.iterrows():
        score, status = calculate_retail_score(row)
        scores.append(score)
        statuses.append(status)
    df['Score'] = scores
    df['Status'] = statuses
    st.dataframe(df)
    st.bar_chart(df['Status'].value_counts())
    st.download_button("📥 Download Results", df.to_csv(index=False), file_name="retail_scores.csv")

# --- Cybersecurity ---
def calculate_cybersecurity_score(row):
    score = (
        row['threat_detection_score'] * 0.4 +
        row['user_risk_score'] * 0.3 +
        row['response_automation_level'] * 0.3
    )
    if score >= 80:
        status = "Cyber Secure"
    elif score >= 50:
        status = "Moderate Risk"
    else:
        status = "High Risk"
    return round(score, 2), status

def cybersecurity_dashboard():
    st.title("🛡️ Cybersecurity")
    df = pd.read_csv("Cybersecurity_Score_Mock.csv")
    scores, statuses = [], []
    for _, row in df.iterrows():
        score, status = calculate_cybersecurity_score(row)
        scores.append(score)
        statuses.append(status)
    df['Score'] = scores
    df['Status'] = statuses
    st.dataframe(df)
    st.bar_chart(df['Status'].value_counts())
    st.download_button("📥 Download Results", df.to_csv(index=False), file_name="cybersecurity_scores.csv")

# --- Travel ---
def calculate_travel_score(row):
    score = (
        row['demand_forecasting_accuracy'] * 0.4 +
        row['pricing_optimization'] * 0.3 +
        row['personalization_level'] * 0.3
    )
    if score >= 80:
        status = "AI Travel Innovator"
    elif score >= 50:
        status = "Moderate AI Use"
    else:
        status = "Traditional Travel"
    return round(score, 2), status

def travel_dashboard():
    st.title("✈️ Travel")
    df = pd.read_csv("Travel_Score_Mock.csv")
    scores, statuses = [], []
    for _, row in df.iterrows():
        score, status = calculate_travel_score(row)
        scores.append(score)
        statuses.append(status)
    df['Score'] = scores
    df['Status'] = statuses
    st.dataframe(df)
    st.bar_chart(df['Status'].value_counts())
    st.download_button("📥 Download Results", df.to_csv(index=False), file_name="travel_scores.csv")

# --- Social Sector ---
def calculate_social_sector_score(row):
    score = (
        row['targeting_accuracy'] * 0.4 +
        row['impact_reporting_quality'] * 0.3 +
        row['donor_engagement_score'] * 0.3
    )
    if score >= 80:
        status = "High Impact"
    elif score >= 50:
        status = "Emerging Potential"
    else:
        status = "Needs Strengthening"
    return round(score, 2), status

def social_sector_dashboard():
    st.title("🤝 Social Sector")
    df = pd.read_csv("Social_Sector_Score_Mock.csv")
    scores, statuses = [], []
    for _, row in df.iterrows():
        score, status = calculate_social_sector_score(row)
        scores.append(score)
        statuses.append(status)
    df['Score'] = scores
    df['Status'] = statuses
    st.dataframe(df)
    st.bar_chart(df['Status'].value_counts())
    st.download_button("📥 Download Results", df.to_csv(index=False), file_name="social_sector_scores.csv")
