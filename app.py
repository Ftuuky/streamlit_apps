import streamlit as st
import pandas as pd
import numpy as np

st.title('Parisian Trees')

HEIGHT_COLUMN = 'height_m'
TYPE_COLUMN = 'tree_type'
DATA = ("https://docs.google.com/spreadsheets/d/1_tncRQH_qM2fCEk6OkZgrCWol8f3ZHrHEaMOFZkLJSw/edit?usp=sharing")

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA, nrows=nrows)
    return data

data_load_state = st.text('Loading dataset...')
data = load_data(154626)
data_load_state.text("Dataset is ready!")

if st.checkbox('Show raw dataset'):
    st.subheader('Raw dataset')
    #st.dataframe(data.style.highlight_max(axis=0))
    st.write(data)

app_mode = st.selectbox("Choose a type of tree", ['Aesculus', 'Acer','Sophora', 'Prunus', 'Pyrus', 'Tilia', 'Quercus', 'Platanus', 'Pinus', 'Corylus', 'Fraxinus', 'Celtis', 'Populus', 'Other'])

height_to_filter = st.slider('Select tree height', 1, 22, 10)
filtered_data = data[(data[HEIGHT_COLUMN] == height_to_filter) & (data[TYPE_COLUMN] == app_mode)]

st.subheader('Map of %s trees with height of %s meters' % (app_mode, height_to_filter))
st.map(filtered_data)
