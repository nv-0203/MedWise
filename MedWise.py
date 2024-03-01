import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('Saved Models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('Saved Models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('Saved Models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    # Adding a larger font heading for "MedWise"
    st.image('Images/img1.jpeg', width=200)
    #st.title('MedWise')
    # Adding a smaller font for "Multiple Disease Prediction System"
    #st.markdown('*Multiple Disease Prediction System*')
    st.markdown("<h1 style='font-size: 36px;'>MedWise</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>A Multiple Disease Prediction System</p>", unsafe_allow_html=True)
    selected = option_menu('',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction ')
    st.markdown("<p style='font-size: 24px;'> (Using Random Forest Classifier) </p>", unsafe_allow_html=True)
    st.markdown("<div style='padding-bottom: 20px;'></div>", unsafe_allow_html=True)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction ')
    st.markdown("<p style='font-size: 24px;'> (Using Logistic Regression) </p>", unsafe_allow_html=True)
    st.markdown("<div style='padding-bottom: 20px;'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title('Parkinsons Prediction ')
    st.markdown("<p style='font-size: 24px;'> (Using Linear SVM) </p>", unsafe_allow_html=True)
    st.markdown("<div style='padding-bottom: 20px;'></div>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz) - Average vocal fundamental frequency')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz) - Maximum vocal fundamental frequency')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz) - Minimum vocal fundamental frequency')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%) - Measure of variation in fundamental frequency (%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs) - Measure of variation in fundamental frequency (Absolute)')

    with col1:
        RAP = st.text_input('MDVP:RAP - Measure of variation in fundamental frequency (Relative Average Perturbation)')

    with col2:
        PPQ = st.text_input('MDVP:PPQ - Measure of variation in fundamental frequency (Five-Point Period Perturbation Quotient)')

    with col3:
        DDP = st.text_input('Jitter:DDP - Measure of variation in fundamental frequency (Jitter: Difference, Delta, or DDP)')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer - Measure of variation in amplitude')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB) - Measure of variation in amplitude (dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3 - Measure of variation in amplitude (APQ3)')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5 - Measure of variation in amplitude (APQ5)')

    with col3:
        APQ = st.text_input('MDVP:APQ - Measure of variation in amplitude')

    with col4:
        DDA = st.text_input('Shimmer:DDA - Measure of variation in amplitude (DDA)')

    with col5:
        NHR = st.text_input('NHR - Measure of ratio of noise to tonal components in the voice')

    with col1:
        HNR = st.text_input('HNR - Measure of ratio of noise to tonal components in the voice')

    with col2:
        RPDE = st.text_input('RPDE - Nonlinear dynamical complexity measure')

    with col3:
        DFA = st.text_input('DFA - Signal fractal scaling exponent')

    with col4:
        spread1 = st.text_input('spread1 - Nonlinear measure of fundamental frequency variation')

    with col5:
        spread2 = st.text_input('spread2 - Nonlinear measure of fundamental frequency variation')

    with col1:
        D2 = st.text_input('D2 - Nonlinear dynamical complexity measure')

    with col2:
        PPE = st.text_input('PPE - Nonlinear measure of fundamental frequency variation')
        
    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
