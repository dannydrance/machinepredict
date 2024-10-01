# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/user/Desktop/Anaconda Courses/ML deployment/my_deployment/trained_model.sav','rb'))

# Creating a function for prediction
def diabetes_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      return 'Maintenance is not Needed'
    else:
      return 'Maintenance is Needed Within 30 Days'  
      
  # create a main function
def main():
    # A title of a user interface
    st.title('PREDICTIVE MAINTENANCE USING LSTM ON SENSOR DATA')
    # Getting the input from the user
        
    Pregnancies=st.text_input('Select Machine Name')
    Glucose=st.text_input('Cycle')
    BloodPressure=st.text_input('Setting One')
    SkinThickness=st.text_input('Setting Two')
    Insulin=st.text_input('Setting Three')
    BMI=st.text_input('Temperature Sensors')
    DiabetesPedigreeFunction=st.text_input('Pressure Sensors')
    Age=st.text_input('Flow Sensors')
    
    # Codes for prediction
    diagnosis = ''
    # Creating a button for prediction  
    if st.button('Maintenance Peredict Result'):
        diagnosis= diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    