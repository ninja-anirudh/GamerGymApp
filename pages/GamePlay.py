import streamlit as st
import pandas as pd

##################################################################
# This section is for the header 
# This will have a Logo, Name of page, Welcome message/Sign out
##################################################################
header1, header2, header3, = st.columns(3, gap='large')
with header1:
    st.image('Logo.png')
    
with header2:
    st.markdown("## Game Play")

with header3:
    st.markdown('##### Welcome: Gamer \n ##### Sign Out')

st.markdown('***')

st.markdown('###### Connected to bluetooth')
st.image('BlueTooth.png')

##################################################################
# Select machine
##################################################################
st.markdown('###### Select Machine')

ExcerciseMachine = st.selectbox(
    '',
    ('Bike', 'TreadMill', 'Elliptical'))

st.image(ExcerciseMachine+'.png')

##################################################################
# Select environment
##################################################################

st.markdown('###### Select environment')

Enviornment = ''

Forest, Ocean, Lava, Custom = st.columns(4, gap='small') 

with Forest:
    st.image('Forest.png')
    if st.button('Forest'):
        Enviornment = 'Forest'

with Ocean:
    st.image('Ocean.png')
    if st.button('Ocean'):
        Enviornment = 'Ocean'

with Lava:
    st.image('Lava.png')
    if st.button('Lava'):
        Enviornment = 'Lava'

with Custom:
    st.image('Custom.png')
    if st.button('Custom'):
        Enviornment = 'Custom'

st.markdown('You selected: '+Enviornment)