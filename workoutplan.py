import streamlit as st
import google.generativeai as genai

import os

api_key = os.getenv("API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Diet & Workout Recommendation")


name = st.text_input("Enter your Name")
age = st.number_input("Age", min_value=10, max_value=100, step=1)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, step=0.1)
height_ft = st.number_input("Height (ft)", min_value=1, max_value=9, step=1)
height_in = st.number_input("Height (inch)", min_value=0, max_value=12, step=1)
body_pref = st.selectbox("Body Preference", ["Lose Weight", "Maintain Weight", "Gain Muscle"])
exercise_timing = st.selectbox("Preferred Exercise Time", ["Morning", "Afternoon", "Evening"])

if st.button("Get My Plan"):
    prompt = f"Write a plan for {name} .my body {age} years old , {weight} , {height_ft} feet , {height_in} inch , {body_pref}"
    response = model.generate_content(prompt)
    st.subheader("My Workout Plan:")
    st.write(response.text)
