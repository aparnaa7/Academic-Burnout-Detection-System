import streamlit as st
import pandas as pd


# Sidebar Component


def show_sidebar():

    st.sidebar.title("📘 About Project")

    st.sidebar.info(
        """
Academic Burnout Detection System

This AI system predicts student burnout
based on study habits, sleep, stress level,
assignment load, and attendance.

Technologies Used:
• Python
• Machine Learning
• Streamlit
"""
    )

    st.sidebar.markdown("---")
    st.sidebar.write("👨‍💻 Developed by CSE Students")



# Suggestion Component

def show_suggestions(level):

    st.subheader("Smart Suggestions")

    if level == "Low":
        st.write("✅ Maintain current routine")
        st.write("✅ Keep balanced study schedule")

    elif level == "Medium":
        st.write("⚠️ Take regular breaks")
        st.write("⚠️ Improve sleep habits")
        st.write("⚠️ Reduce workload slightly")

    else:
        st.write("🚨 High burnout detected")
        st.write("• Take proper rest")
        st.write("• Reduce academic pressure")
        st.write("• Talk with mentors")
        st.write("• Practice physical activity")


# Prediction Function


def predict_burnout(study, sleep, stress, assignment, attendance):

    try:

        # High burnout condition
        if stress >= 8 or sleep <= 4 or assignment >= 8:
            level = "High"
            score = 80

        # Medium burnout condition
        elif stress >= 5 or sleep <= 6 or assignment >= 5:
            level = "Medium"
            score = 50

        # Low burnout condition
        else:
            level = "Low"
            score = 20

        return score, level

    except Exception as e:
        print("Prediction Error:", e)
        return 0, "Low"

# Streamlit App


st.set_page_config(page_title="Academic Burnout Detection", page_icon="📚")

st.title("📚 Academic Burnout Detection System")

# Sidebar
show_sidebar()

# Student name
name = st.text_input("Enter Student Name")

st.subheader("Enter Student Details")

# Inputs
study_hours = st.slider("Study Hours per day", 0, 12, 5)
sleep_hours = st.slider("Sleep Hours per day", 0, 12, 7)
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
assignment_load = st.slider("Assignment Load (1-10)", 1, 10, 5)
attendance = st.slider("Attendance Percentage", 0, 100, 75)

# Prediction
if st.button("Predict Burnout"):

    burnout_score, level = predict_burnout(
        study_hours,
        sleep_hours,
        stress_level,
        assignment_load,
        attendance
    )

    st.subheader(f"Result for {name if name else 'Student'}")

    if level == "Low":
        st.success("Burnout level - Low 😊")

    elif level == "Medium":
        st.warning("Burnout level - Moderate ⚠️")

    else:
        st.error("Burnout level - High 🚨")

    percent = min(100, burnout_score)

    # Visualization Data
    data = pd.DataFrame({
        "Category": [
            "Study Hours",
            "Sleep Hours",
            "Stress Level",
            "Assignment Load",
            "Attendance"
        ],
        "Value": [
            study_hours,
            sleep_hours,
            stress_level,
            assignment_load,
            attendance
        ]
    })

    st.subheader("Student Activity Overview")
    st.bar_chart(data.set_index("Category"))

    # Suggestions
    show_suggestions(level)

    # Report
    report = f"""
Academic Burnout Report

Student Name: {name}

Study Hours: {study_hours}
Sleep Hours: {sleep_hours}
Stress Level: {stress_level}
Assignment Load: {assignment_load}
Attendance: {attendance}

Burnout Score: {burnout_score}
Burnout Level: {level}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="burnout_report.txt"
    )

st.markdown("---")
st.write("Developed using Streamlit | Academic Burnout Detection System")
