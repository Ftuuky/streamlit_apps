import streamlit as st
import pandas as pd
import numpy as np

st.title('Parisian Trees')

#fetch some data
HEIGHT_COLUMN = 'height_m'
TYPE_COLUMN = 'tree_type'
DATA = ("https://docs.google.com/spreadsheets/d/1_tncRQH_qM2fCEk6OkZgrCWol8f3ZHrHEaMOFZkLJSw/edit?usp=sharing")

#allow streamlit to cache the loaded data
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA, nrows=nrows)
    return data

data_load_state = st.text('Loading dataset...')
data = load_data(154626)
data_load_state.text("Dataset is ready!")

#inspect raw data
if st.checkbox('Show raw dataset'):
    st.subheader('Raw dataset')
    st.write(data)

#two possible filters; by tree type and by tree height
#tree type is selected from a dropdown menu and height with a slider
app_mode = st.selectbox("Choose a type of tree", ['Aesculus', 'Acer','Sophora', 'Prunus', 'Pyrus', 'Tilia', 'Quercus', 'Platanus', 'Pinus', 'Corylus', 'Fraxinus', 'Celtis', 'Populus', 'Other'])
height_to_filter = st.slider('Select tree height', 1, 22, 10)

#filter the data with the above conditions
filtered_data = data[(data[HEIGHT_COLUMN] == height_to_filter) & (data[TYPE_COLUMN] == app_mode)]

st.subheader('Map of %s trees with height of %s meters' % (app_mode, height_to_filter))
st.map(filtered_data)
