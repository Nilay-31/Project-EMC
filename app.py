# Importing necessary libraries
import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model_path = 'email_open_prediction_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Page title
st.title("Email Marketing Campaign Prediction")
st.write("Predict if a customer will open their emails based on their past behavior and attributes.")

# Sidebar for user input
st.sidebar.header("User Input Parameters")

def user_input_features():
    Customer_Age = st.sidebar.slider("Customer Age", 18, 80, 30)
    Emails_Opened = st.sidebar.slider("Emails Opened", 0, 100, 10)
    Emails_Clicked = st.sidebar.slider("Emails Clicked", 0, 100, 5)
    Purchase_History = st.sidebar.slider("Purchase History (in $)", 0, 5000, 1000)
    Time_Spent_On_Website = st.sidebar.slider("Time Spent On Website (in minutes)", 0, 300, 50)
    Days_Since_Last_Open = st.sidebar.slider("Days Since Last Open", 0, 365, 30)
    Customer_Engagement_Score = st.sidebar.slider("Customer Engagement Score", 0, 100, 50)
    Device_Type = st.sidebar.selectbox("Device Type", options=[0, 1, 2], format_func=lambda x: ["Desktop", "Mobile", "Tablet"][x])
    Clicked_Previous_Emails = st.sidebar.selectbox("Clicked Previous Emails", options=[0, 1], format_func=lambda x: ["No", "Yes"][x])

    data = {
        'Customer_Age': Customer_Age,
        'Emails_Opened': Emails_Opened,
        'Emails_Clicked': Emails_Clicked,
        'Purchase_History': Purchase_History,
        'Time_Spent_On_Website': Time_Spent_On_Website,
        'Days_Since_Last_Open': Days_Since_Last_Open,
        'Customer_Engagement_Score': Customer_Engagement_Score,
        'Device_Type': Device_Type,
        'Clicked_Previous_Emails': Clicked_Previous_Emails
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Display user input
st.subheader("User Input Parameters")
st.write(input_df)

# Predict using the model
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# Display prediction
st.subheader("Prediction")
st.write("Opened Previous Emails" if prediction[0] == 1 else "Did Not Open Previous Emails")

# Display prediction probability
st.subheader("Prediction Probability")
st.write(prediction_proba)
