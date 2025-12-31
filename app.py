import matplotlib.pyplot as plt 
import streamlit as st
from planner import predict_hours

# ---------- Page Config ----------
st.set_page_config(
    page_title="Smart Study Planner",
    page_icon="🎓",
    layout="centered"
)

# ---------- Header ----------
st.markdown(
    "<h1 style='text-align:center;'>🎓 Smart Study Planner</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;color:gray;'>ML-powered daily study recommendations</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- Input Section ----------
st.subheader("📥 Study Details")

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input("📘 Subject Name", placeholder="e.g., Machine Learning")
    marks = st.slider("📝 Last Test Marks", 0, 100, 50)

with col2:
    difficulty_label = st.selectbox(
        "⚙️ Subject Difficulty",
        ["Easy", "Medium", "Hard"]
    )
    days_left = st.number_input("⏳ Days Left for Exam", min_value=1, max_value=120, value=10)

difficulty_map = {"Easy": 1, "Medium": 2, "Hard": 3}
difficulty = difficulty_map[difficulty_label]

st.markdown("---")

# ---------- Action ----------
if st.button("🚀 Generate Smart Plan", use_container_width=True):

    with st.spinner("Analyzing your performance..."):
        hours = predict_hours(marks, difficulty, days_left)

    st.success("✅ Smart study plan generated")

    # Result card (your existing code here)

    # Smart insight (your existing if-elif-else here)

    # 📊 PASTE THIS PART BELOW
    st.subheader("📊 Study Trend Analysis")

    marks_data = [20, 40, 60, 80, marks]
    hours_data = [
        predict_hours(20, difficulty, days_left),
        predict_hours(40, difficulty, days_left),
        predict_hours(60, difficulty, days_left),
        predict_hours(80, difficulty, days_left),
        hours
    ]

    fig, ax = plt.subplots()
    ax.plot(marks_data, hours_data, marker='o')
    ax.set_xlabel("Marks")
    ax.set_ylabel("Recommended Study Hours / Day")
    ax.set_title("Marks vs Study Hours Trend")

    st.pyplot(fig)


    hours = predict_hours(marks, difficulty, days_left)

    st.success("✅ Smart study plan generated")

    # Result Card
    st.markdown(
        f"""
        <div style="
            background-color:#f6f9ff;
            padding:20px;
            border-radius:12px;
            border-left:6px solid #4f8bf9;
        ">
            <h3>📘 {subject or 'Selected Subject'}</h3>
            <h2 style="color:#4f8bf9;">⏱ {hours} hours / day</h2>
            <p style="color:gray;">
                Based on your performance, subject difficulty, and exam timeline.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Smart Insight
if marks < 50:
    st.warning("⚠️ Focus more on basics and revise daily.")
elif marks < 75:
    st.info("ℹ️ You are doing well. Stay consistent.")
else:
    st.success("🌟 Strong subject! Maintain with light revision.")

