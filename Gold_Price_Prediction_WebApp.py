# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:19:42 2024

@author: prachet
"""
import numpy as np
import pickle
import streamlit as st

#loading. the saved model
loaded_model = pickle.load(open('C:/Users/prachet/OneDrive - Vidyalankar Institute of Technology/Desktop/Coding/Machine Learning/ML-Project-8-Gold Price Prediction/gold_price_prediction_model.sav','rb'))

#creating a function for prediction

def gold_price_prediction(input_data):

    #changing the input data to numpy
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting on 1 instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)

    return prediction[0]
  
    
  
def main():
    
    #giving a title
    st.title('Gold Price Prediction Web App')

    #getting input data from user
    SPX = st.number_input("SPX")
    USO = st.number_input("USO")
    SLV = st.number_input("SLV")	
    EUR_USD = st.number_input("EUR/USD")
    
    # code for prediction
    price = ''
    
    #creating a button for Prediction
    if st.button('Predict Gold Price'):
        price = gold_price_prediction((SPX,USO,SLV,EUR_USD))
        
    st.success('The Predicted Price: '+ str(price)+'$')
    
    
    
if __name__ == '__main__':
    main()
    
    
