from pycaret.regression import *
import streamlit as st 
import pandas as pd 
import numpy as np 

model = load_model('deployment-nummer-1')

def predict(model, input_df):
    predictions_df = predict_model(estimator = model, data= input_df)
    print(predictions_df)
    predictions = predictions_df['prediction_label'][0]
    return predictions

def run():
    from PIL import Image
    # image = Image.open('https://github.com/pycaret/pycaret-streamlit-google/blob/master/logo.png')
    # image_hospital = Image.open('https://github.com/pycaret/pycaret-streamlit-google/blob/master/hospital.jpg')

    # st.image(image, use_column_width = False)

    add_selectbox = st.sidebar.selectbox(
        'how would you like to predict?',
        ('online','batch')
    )

    st.sidebar.info('this app is created to predict patient hospital charges')
    st.sidebar.success('https://www.pycaret.org')

    # st.sidebar.image(image_hospital)

    st.title('insurance charges prediction app')

    if add_selectbox == 'online':
        age = st.number_input('age', min_value= 1, max_value = 100, value = 25)
        sex = st.selectbox('sex', ('M', 'F'))

        bmi = st.number_input('BMI', min_value = 10, max_value = 50, value = 10)

        children = st.selectbox('Children',[0,1,2,3,4,5,6])

        if st.checkbox('smoker'):
            smoker = 'yes'
        else: 
            smoker = 'no'

        region = st.selectbox('Region', ['northeast', 'southwest', 'northwest', 'southeast'])

        output = ''

        input_dict = {
            'age':age,
            'sex':sex,
            'bmi':bmi,
            'children':children,
            'smoker':smoker,
            'region':region
        }
        input_df = pd.DataFrame([input_dict])

        if st.button('predict'):
            output = predict(model = model, input_df = input_df)
            output = '$ ' + str(output)

        st.success(
            'The output is {}'.format(output)
        )

    if add_selectbox == 'batch':
        file_upload = st.file_uploader(' upload csv for predictions', type=['csv'])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator = model, data= data)
            st.write(predictions)
            
run()
