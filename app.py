# Import the necessary libraries
import streamlit as st
from fastapi import FastAPI
import joblib

# Load the pre-trained model
model = joblib.load('student-performance-model.pkl')

# Create the FastAPI app
app = FastAPI()

# Define the endpoint for the model
@app.post("/predict")
def predict(data: List[float]):
    '''
    This function uses the serves the model to make a prediction
    using the input data
    '''
    prediction = model.predict(data)
    return {"prediction": prediction}

# Create the Streamlit app
def main():
    '''
    This is the principal function used to run the streamlit frontend
    '''
    st.title("Binary Classifier Model for Student performance")

    #add a home page whicha ask to login as admin or user
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)
    st.markdown("Enter the input data below to get a prediction")
    
    # Get the input data from the user
    data = st.text_input("Input data (comma-separated):")
    data = [float(x) for x in data.split(",")]

    # Use the FastAPI app to make a prediction
    response = app.post("/predict", data=data)
    prediction = response.json()["prediction"]

    # Display the result to the user
    st.write(f"Prediction: {prediction}")

# Run the Streamlit app
if __name__ == '__main__':
    main()
