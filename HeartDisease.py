import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import pickle 
import streamlit as st

model=pickle.load(open('HeartDiseaseLogistic.pkl','rb'))

def prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal):
    #preprocessing user input 
    if sex == '1':
        sex=1
    else:
        sex=0

    if cp == '1':
        cp=1
    else: 
        cp=0
    
    if fbs == '1':
        fbs =1
    else: 
        fbs=0
    
    if restecg == '1':
        restecg =1
    elif restecg == '0':
        restecg=0
    else:
        restecg = 2

    if exang == '1':
        exang =1
    else:
        exang=0

    if slope == '1':
        slope=1
    else:
        slope=0

    if ca == '1':
        ca=1
    elif ca == '0':
        ca=0
    elif ca == '2':
        ca=2
    elif ca == '3':
        ca=3
    else:
        ca=4

    if thal == '1':
        thal = 1
    else:
        thal=0



    #making predictons 
    prediction=model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal]])
    if prediction==0:
        pred = "You don't have a heart disease"
    else:
        pred="You have a heart disease. See a doctor immediately"
    return pred

       #this is the main function inwhich we define our webpage 
def main():
    #front end elemnts of the web page
    html_temp="""  
    <div style="background-color:green;padding:13px">
    <h1 style = "color:black;text-align:center;">Osadiapet Loan Prediction Machine Learning App</h1>
    </div>
    """ 
    #display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    #the following lines creates boxes inwhich user can enter data required to make prediction
    age=st.number_input('Age of patient')
    sex=st.selectbox('sex',('Male','Female'))
    cp=st.selectbox('Chest Pain Type', ('1=Not Severe','2=Somewhat Severe','3=Severe','4=Very Severe'))
    trestbps=st.number_input('resting blood pressure (in mm Hg on admission to the hospital)')
    chol=st.number_input('serum cholestoral in mg/dl')
    fbs=st.selectbox('fasting blood sugar > 120 mg/dl)', ('1 = true', '0 = false'))
    restecg=st.selectbox('Resting Electrocardiographic Results',('1=Low','Moderate','High'))
    thalach=st.number_input('Maximum Heart Rate Achieved')
    exang=st.selectbox('exercise induced angina',('1=Yes','0=No'))
    oldpeak=st.number_input('ST depression induced by exercise relative to rest')
    slope=st.selectbox('the slope of the peak exercise ST segment',('1=Yes','0=No'))
    ca=st.number_input('number of major vessels (0-3) colored by flourosopy(0-4)')
    thal=st.selectbox('thal',('3=normal', '6=fixed defect', '7=reversable defect'))
    result=""

    #when 'predict' is clicked, make the prediction and store it

    if st.button("Predict"):
        result=prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal)
        st.success('Than You.  {}'.format(result))
if __name__=='__main__':
        main()






    