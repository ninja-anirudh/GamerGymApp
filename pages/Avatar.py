import streamlit as st
import pandas as pd
import numpy as np


##################################################################
# This section is for the header 
# This will have a Logo, Name of page, Welcome message/Sign out
##################################################################
header1, header2, header3, = st.columns(3, gap='large')
with header1:
    st.image('Logo.png')
    
with header2:
    st.markdown("## Avatar")

with header3:
    st.markdown('##### Welcome: Gamer \n ##### Sign Out')

st.markdown('***')

##################################################################
# Two columns one for profile creation, other to see it
##################################################################

CreateProfile, SeeProfile = st.columns(2, gap='small')

with CreateProfile:
    UserName = st.text_input('User Name')

    DateOfBirth = st.date_input('Enter date of birth')

    profile_pic = ''
    profilepicavailable = False

    with st.container():
        profile_pic_select = st.file_uploader("Choose a profile picture")
        profile_pic_cam = st.camera_input("Take a picture")

        if st.button("Update pic"):
            if profile_pic:
                profile_pic = profile_pic_select
                profilepicavailable = True
            else:
                if profile_pic_cam:
                    profile_pic = profile_pic_cam
                    profilepicavailable = True
                else:
                    profile_pic = '' 

with SeeProfile:
    st.markdown('##### Welcome: '+ UserName)
    st.markdown('Level Gold 1000/1000')
    if not(profilepicavailable):
        st.markdown('No profile picture available')
    else:
        st.image(profile_pic)

    st.markdown('##### Your statistics')
    st.markdown('You have generated 1000 Watts')
    st.markdown('You need to generate 9000 more Watts to Platinum')

    BikeTab, TreadTab, EllipTab = st.tabs(["Bike", "TreadMill", "Elliptical"])

    with BikeTab:
        bike_chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["a", "b", "c"])
        st.bar_chart(bike_chart_data)

    with TreadTab:
        tread_chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["a", "b", "c"])
        st.bar_chart(tread_chart_data)
        
    with EllipTab:
        ellip_chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["a", "b", "c"])
        st.bar_chart(ellip_chart_data)
    