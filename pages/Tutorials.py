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
    st.markdown("## Tutorials")

with header3:
    st.markdown('##### Welcome: Gamer \n ##### Sign Out')

st.markdown('***')

##################################################################
# This will have a videos about renewable energy and help on app
##################################################################

st.info('Watch videos about renewable energy and earn points',icon="ℹ️")

energyvideos, helpsection = st.columns(2,gap='large')

with energyvideos:
    st.markdown('#### Renewable energy videos')

    with st.expander('All about renewable energy'):
        st.video('https://www.youtube.com/watch?v=RLYaWgQysTA')

    with st.expander('Why pollution is a problem'):
         st.video('https://www.youtube.com/watch?v=KeWYaL85SNw')

    with st.expander('How pollution is made'):
         st.video('https://www.youtube.com/watch?v=mR47Zq9KgMU')

    with st.expander('Why renewable energy is better'):
         st.video('https://www.youtube.com/watch?v=y5a8-g4RKKQ')

    with st.expander('How we can generate renewable energy'):
         st.video('https://www.youtube.com/watch?v=imoIzpReobE')   

with helpsection:
    st.markdown('#### Gamer Gym help')

    with st.expander('Make an avatar'):
        st.markdown('Make an avatar by going to Avatar page - Enter your name, date of birth, upload a cool profile picture')

    with st.expander('How to play'):
        st.markdown('Connect your energy generating excercise equipment to the app by blue tooth, select a game mode and play')

    with st.expander('Connect your excercise device to the app'):
        st.markdown('Connect your energy generating excercise equipment to the app by blue tooth')

    with st.expander('Change settings in the app'):
        st.markdown('You can change your user name in the avatar page, you can also change your profile picture on the same page')

    with st.expander('Game play mode'):
        st.markdown('Go to game play mode page, select your excecise machine type, and game play mode like ocean, ,forest, lava etc')