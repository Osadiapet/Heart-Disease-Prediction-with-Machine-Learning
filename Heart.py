
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('HeartRF.pkl', 'rb') 
classifier = pickle.load(pickle_in)

def prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):

     # Making predictions 
    prediction = classifier.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
     
    if prediction == 0:
        pred = "don't have a heart disease"
    else:
        pred = 'have a heart disease. Please see your doctor immediately!'
    return pred

    # this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Osadiapet Heart Disease Machine Learning App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    # following lines create boxes in which user can enter data required to make prediction 
    Age=st.slider('Select Age', 0, 100, 50)
    sex = st.radio("Gender",('Male','Female'))
    cp = st.radio("Chest Pain Experienced",('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'))
    trestbps= st.slider('Resting Blood Pressure', 0, 200, 50)
    chol=st.slider('Enter Cholesterol Level', 0, 700, 50)
    fbs=st.radio("Fasting Blood Sugar",('True','False'))
    restecg = st.radio("Resting Electrocardiographic Measurement",('Normal','having ST-T Wave Abnormality', 'showing probable or definite left ventricular hypertrophy by Estes'))
    thalach = ('Maximum Heart Rate Achieved', 0, 250, 50)
    exang = st.radio("Exercise Induced Angina",('Yes','No'))
    oldpeak = ('ST depression induced by exercise relative to rest', 0, 10, 2)
    slope = st.radio("Slope of the Peak Exercise ST Segment",('Upslopping', 'Flat', 'Down Slopping'))
    ca= ('Number of Major Vessels', 0, 5, 1)
    thal =  st.radio("Thalasemia (Blood Disorder)",('Normal','Fixed Defect', 'Reversable Defect'))

    result =""

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Age, sex,cp, trestbps, chol,fbs, restecg, thalach, exang, oldpeak, slope, ca, thal) 
        st.success('You {}'.format(result))
       
if __name__=='__main__': 
    main()


