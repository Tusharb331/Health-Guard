import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration
st.set_page_config(page_title = "Health Gaurd", layout = "wide")

# path of working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading of the save model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System", ["Diabetes Prdiction", "Heart Disease Prediction"], menu_icon = "hospital-fill", icons = ["activity", "heart"], default_index = 0)

# diabetes prediction page
if selected == "Diabetes Prdiction":

    # page title
    st.title("Diabetes Prdiction Using ML")

    # getting input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        pregnancies = st.text_input("Number of Pregnancies")
        insulin = st.text_input("Insulin Level")

    with col2:
        glucose = st.text_input("Glucose Level")
        bmi = st.text_input("BMI Value")

    with col3:
        blood_pressure = st.text_input("Blood Pressure Value")
        dpf = st.text_input("Diabetes Pedigree Function Value")

    with col4:
        skin_thickness = st.text_input("Skin Thickness Value")
        age = st.text_input("Person Age")

    # backend logic
    diab_diagnosis = ""

    # creation of a button
    if st.button("Diabetes Text Result"):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
        user_input = [float(x) for x in user_input]
        diabetes_prediction = diabetes_model.predict([user_input])
        if diabetes_prediction[0] == 1:
            diab_diagnosis = "Person is Diabetic"
        else:
            diab_diagnosis = "Person is not Diabetic"
        st.success(diab_diagnosis)
    
# heart disease prediction page
if selected == "Heart Disease Prediction":

    # page title
    st.title("Heart Disease Prdiction Using ML")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        age = st.text_input("Age")
        chol = st.text_input("Serum cholertrol in mg/dl")
        exang = st.text_input("Excercise induces angina")
        thal = st.text_input("Thal: 0 => Normal; 1=> fixed defect")

    with col2:
        sex = st.text_input("Gender")
        fbs = st.text_input("Fasting blood sugar")
        oldpeak = st.text_input("ST depression induced by excercise")

    with col3:
        cp = st.text_input("Cheast pain type")
        restecg = st.text_input("Resting electrocardiographic result")
        slope = st.text_input("Slope of the peak excercise ST segment")

    with col4:
        trestbps = st.text_input("Resting blood pressure")
        thalach = st.text_input("Maximum heart rate achieved")
        ca = st.text_input("Major vessels colored by flourosopy")

    # backendlogic
    heart_diagnosis = ""

    # creation of a button
    if st.button("Heart Disease Text Result"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_model_prediction = heart_model.predict([user_input])
        if heart_model_prediction[0] == 1:
            heart_diagnosis = "Person is Unhealthy"
        else:
            heart_diagnosis = "Person is Healthy"
        st.success(heart_diagnosis)

# parkinsins prediction page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinsons Prediction Using ML")

