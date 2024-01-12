# MedWise - A Disease Prediction Streamlit App

Welcome to MedWise, a web application for predicting Diabetes, Parkinson's Disease, and Heart Disease. This project utilizes custom machine learning models seamlessly integrated into a Streamlit web app to provide efficient predictions.

## Overview

MedWise is designed to predict three different diseases using specific machine learning models:

- Diabetes Prediction using [Random Forest Classifier](Trained%20Models/diabetes.ipynb)  
- Heart Disease Prediction using [Linear SVM Model](Trained%20Models/heart.ipynb)  
- Parkinson's Prediction using [Logistic Regression Model](Trained%20Models/Parkinsons.ipynb) 
 

## Usage

The application is deployed and can be accessed [here](https://medwise-nv-0203.streamlit.app/).  
The user interface is intuitive and user-friendly, leveraging the Streamlit Option Menu for easy navigation. 

## Libraries Used

- **streamlit**: Enabled the creation of a user-friendly web application. Leveraged Streamlit's simple and intuitive API to design the user interface.

- **scikit-learn**: Provided the implementation of machine learning models. The Random Forest Classifier, Linear SVM Model, and Logistic Regression Model are all implemented using scikit-learn.

- **pickle**: Employed in MedWise for model persistence. After training the machine learning models, they are serialized using pickle and saved to disk. This allows for quick and easy loading of pre-trained models within the Streamlit app, ensuring that predictions can be made without the need for retraining each time the application is launched.

- **pandas**: Used in handling and processing the datasets used in MedWise.


