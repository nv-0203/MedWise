# MedWise - A Disease Prediction Streamlit App

Welcome to MedWise, a web application for predicting Diabetes, Parkinson's Disease, and Heart Disease. This project utilizes custom machine learning models seamlessly integrated into a Streamlit web app to provide efficient predictions.

## Overview

MedWise is designed to predict three different diseases using specific machine learning models:

- Diabetes Prediction using a [Soft Voting Classifier](Trained%20Models/diabetes.ipynb)  
- Heart Disease Prediction using a [Bagging Ensembler](Trained%20Models/heart.ipynb)  built on Logistic Regression Model
- Parkinson's Prediction using a [Stacking Classifier](Trained%20Models/Parkinsons.ipynb) with KNN, SVC and Random Forest as base Models, Logistic Regression as the meta model
 

## Usage

The application is deployed and can be accessed [here](https://medwise-nv-0203.streamlit.app/).  
The user interface is intuitive and user-friendly, leveraging the Streamlit Option Menu for easy navigation. 

## Libraries Used

- **streamlit**: Enabled the creation of a user-friendly web application. Leveraged Streamlit's simple and intuitive API to design the user interface.

- **scikit-learn**: used in Parkinson's Prediction. The Random Forest Classifier, Linear SVM Model, KNN and Logistic Regression Model are all implemented and stacked using scikit-learn.
  
- **pycaret**: used in Heart Disease and Diabetes Prediction. Soft Voting Ensembler and Bagging are implemented using it

- **pickle**: Employed in MedWise for model persistence. After training the machine learning models, they are serialized using pickle and saved to disk. This allows for quick and easy loading of pre-trained models within the Streamlit app, ensuring that predictions can be made without the need for retraining each time the application is launched.

- **pandas**: Used in handling and processing the datasets used in MedWise.


