import streamlit as st
import pandas as pd

##################################################################
# This section is for the header 
# This will have a Logo, Name of app, Welcome message/Sign out
##################################################################
header1, header2, header3, = st.columns(3, gap='large')
with header1:
    st.image('Logo.png')
    
with header2:
    st.markdown("## Gamer Gym")

with header3:
    st.markdown('##### Welcome: Gamer \n ##### Sign Out')

st.markdown('***')

###################################################################
## This has the leader board and the Daily challenges
###################################################################

section2_col1, section2_col2 = st.columns(2,gap='large')

with section2_col1:
    DailyChallengedata = [['20 watts', '1/11/23'],['Win one race of medium to hard','1/30/23'],
    ['Watch videos', '12/31/22'],['Winter 2022', '12/31/22'],['Create your own challenges', '12/31/23'] ]
    DailyChallengedf = pd.DataFrame(DailyChallengedata,columns=['Challenge', 'Expiry date'])

    st.markdown('#### Daily challenges')
    st.dataframe(DailyChallengedf,use_container_width=True)

with section2_col2:
    LeaderBoarddata = [[1, 'Joedagreat999',1234],[2, 'Blowout bob669',1233],[3,'lollthedude333',1232], [4,'llloofff999',1231], [5,'lbozoratio200',1230] ]
    LeaderBoarddf = pd.DataFrame(LeaderBoarddata,columns=['Rank','UserName', 'Watts'])

    st.markdown('#### Leader board')
    st.dataframe(LeaderBoarddf,use_container_width=True)
