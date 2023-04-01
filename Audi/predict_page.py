import streamlit as st
import pickle
import numpy as np
import datetime

def load_model():
    with open('saved_data.pkl','rb') as file:
        data = pickle.load(file)
    return data
    
data = load_model()

regressor = data.get('model')
le_fueltype = data.get('le_fueltype')
scaler = data.get('scaler')

def show_predict_page():
    st.title("Audi Car Price Prediction")
    
    st.write("""### We need some information to predict the price""")

    fueltypes = le_fueltype.classes_

   
    now = datetime.datetime.now().year
    year = st.slider("Year",1970,now,2010)

    mileage = st.number_input("Mileage",min_value=0.)

    fueltype = st.selectbox("Fuel Type",fueltypes)
    fueltype = le_fueltype.transform([fueltype])[0]

    tax = st.number_input("tax",min_value=0.)
    
    mpg = st.number_input("mpg",min_value=0.)
    
    engineSize = st.number_input("Engine Size",min_value=0.)

    ok = st.button("Calculate Price")

    if ok:
        X = np.array([[year,mileage,fueltype,tax,mpg,engineSize]])
        X = scaler.transform(X)

        price = regressor.predict(X)

        st.subheader(f"The estimated price is: :blue[€{price[0]:,.2f}]")
