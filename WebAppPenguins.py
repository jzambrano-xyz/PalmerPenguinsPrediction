#The purpose of this code is to display a web app that predicts the species so a penguin using a RandomForestClassifier
#Import the required libraries to run the web app
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

#Write the interface of the Web app using Markdown
st.write("""
# Penguin prediction with **Machine Learning**

Prediction of the species of a _Palmer penguin_ using a **Random Forest Classifier**

Data from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) by _Allison Horst_.
""")

#Create the sidebar for interaction with the user
st.sidebar.header('User input features')

st.set_option('deprecation.showfileUploaderEncoding', False)

st.sidebar.markdown("""
[Example **.csv** input file](https://github.com/jzambrano-xyz/PalmerPenguinsPrediction/blob/master/penguins_example.csv)
""")

#Get the qualitative input features from the user, giving the option to upload a .csv
#or by manual input with the app's sliders
uploaded_file = st.sidebar.file_uploader("Upload your **.csv** file", type=["csv"])
if uploaded_file is not None: #Not an empty file
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
        sex = st.sidebar.selectbox('Sex', ('male', 'female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.6, 43.9) #Min, max, default
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1, 21.5, 17.2) #Min, max, default
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0, 231.0, 201.0) #Min, max, default
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0, 6300.0, 4207.0) #Min, max, default
        data = {'island' : island,
                'bill_length_mm' : bill_length_mm,
                'bill_depth_mm' : bill_depth_mm,
                'flipper_length_mm' : flipper_length_mm,
                'body_mass_g' : body_mass_g,
                'sex' : sex}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

#Combine the user's input features wth the entire penguins dataset
#This combination will be used when encoding
penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species']) #This removes the first column from the cleaned dataset
df = pd.concat([input_df, penguins], axis=0)#Joins the user's input with the cleaned dataset

#Encoding of the ordinal user_input_features
encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]
df = df[:1] #Selects only the first row from the user's input data

#Display in the screen the user's input user input features
st.subheader('User input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting for a .csv file to be uploaded; currently using example parameters (shown below)')
    st.write(df)

#Load the saved classification model from the pickle file
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

#Apply the model to make predictions on the input
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)

#Display the prediction in the screen
st.subheader('Prediction')
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguins_species[prediction])

#Display the probability of the prediction made
st.subheader('Prediction probability')
st.write(prediction_proba)
