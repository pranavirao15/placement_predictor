import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 🎨 Page Config
# -----------------------------
st.set_page_config(
    page_title="🎓 Smart Placement Predictor",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# 🎨 Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
    }
    h1, h2, h3 {
        font-family: 'Trebuchet MS', sans-serif;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 🎓 Title Section
# -----------------------------
st.title("🎓 Smart Placement Predictor")
st.subheader("📊 Predict Your Placement Chances Instantly")

st.write("✨ Enter your academic details in the sidebar to check your placement probability.")

# -----------------------------
# 📊 Sidebar Inputs
# -----------------------------
st.sidebar.header("📝 Input Features")

cgpa = st.sidebar.slider("📚 CGPA", 0.0, 10.0, 7.0)
internships = st.sidebar.slider("💼 Internships", 0, 10, 1)
projects = st.sidebar.slider("🛠️ Projects", 0, 10, 2)
aptitude = st.sidebar.slider("🧠 Aptitude Score", 0, 100, 60)
communication = st.sidebar.slider("🗣️ Communication Skills", 0, 10, 6)

# -----------------------------
# 🧠 Dummy Prediction Logic
# -----------------------------
def predict(cgpa, internships, projects, aptitude, communication):
    score = (
        cgpa * 0.3 +
        internships * 0.2 +
        projects * 0.2 +
        aptitude * 0.2 / 10 +
        communication * 0.1
    )
    return min(score / 10, 1)

# -----------------------------
# 🔮 Prediction Button
# -----------------------------
if st.button("🚀 Predict Placement Chance"):

    probability = predict(cgpa, internships, projects, aptitude, communication)

    st.success(f"🎯 Placement Probability: {round(probability * 100, 2)}%")

    if probability > 0.7:
        st.balloons()
        st.write("🔥 Excellent! You're highly likely to get placed!")
    elif probability > 0.4:
        st.write("👍 Good, but you can improve further!")
    else:
        st.write("⚠️ Focus on improving your skills and experience.")

    # -----------------------------
    # 📊 Visualization
    # -----------------------------
    st.subheader("📈 Performance Breakdown")

    data = pd.DataFrame({
        "Feature": ["CGPA", "Internships", "Projects", "Aptitude", "Communication"],
        "Value": [cgpa, internships, projects, aptitude, communication]
    })

    fig, ax = plt.subplots()
    ax.bar(data["Feature"], data["Value"], color='skyblue')
    ax.set_title("Your Profile Analysis 📊")
    ax.set_ylabel("Values")

    st.pyplot(fig)

# -----------------------------
# 📌 Footer
# -----------------------------
st.markdown("---")
st.write("💡 Built with Streamlit | 🚀 AI Placement Assistant")