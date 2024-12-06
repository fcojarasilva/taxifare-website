import streamlit as st
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
# ** TAXIFARE PREDICTION **
''')


pickup_date = st.date_input("Pickup date", datetime.date(2015,12,22))
pickup_time = st.time_input("Pickup time", datetime.time(12,40,52))
pickup_longitude = st.number_input("Pickup longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.748817)
passenger_count = st.number_input("Passenger count", min_value=1, max_value=6, value=1)




url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('')


if st.button('Predict'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    st.write('Further clicks are not visible but are executed')
else:
    st.write('I was not clicked 😞')
