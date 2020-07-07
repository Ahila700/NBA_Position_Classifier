import streamlit as st
import pandas as pd
import numpy as np

import pickle
from pickle import load

from mod_5_functions import draw_court

import matplotlib.pyplot as plt

from matplotlib.patches import Arc, Circle, Rectangle

import warnings
warnings.filterwarnings('ignore')



st.title("NBA Position Classifier")
st.markdown("This application is a Streamlit dashboard that can be used to check the new position of a modern NBA player as "
            "well as the most similar player to him in the league. Just enter his name below:")

 
# importing csv file
df = pd.read_csv('csv_files/Final_df.csv', index_col = 0)

# importing csv file for shot charts
shot_charts = pd.read_csv('csv_files/2019-20_nba_shot_charts.csv', index_col = 0)


#loading pickled model
model = pickle.load(open('SVM_model','rb'))

# loading dictionary of similar players
similarity_dict = pickle.load(open('Player_similarity_dict', 'rb'))




# creating area to enter player name
player = st.text_area('Enter Player Name')


#once submitted the player name is then put into the csv file and after we remove the additional 

if st.button('Submit'):
    
    new_player = df[df.Player == player]
    new_player.drop(columns = ['Player', 'PLAYER_ID', 'Pos'], inplace = True)
    
    Position = model.predict(new_player)
    
    Similar_player = similarity_dict[player]
    
    shot_chart = shot_charts[shot_charts.PLAYER_NAME == player]
    shot_chart2 = shot_charts[shot_charts.PLAYER_NAME == Similar_player]
    

    st.write('The Players Position is: ' + Position[0])
    st.write('The Most Similar Player is: ' + Similar_player)
    
    plt.figure(figsize=(12,11))
    plt.scatter(shot_chart.LOC_X, shot_chart.LOC_Y, marker = 'o')
    plt.scatter(shot_chart2.LOC_X, shot_chart2.LOC_Y, marker = 'x', alpha = .75)
    plt.title('Shotchart Comparison', fontdict = {'fontsize': 20})
    draw_court(outer_lines=True)
    plt.xlim(-300,300)
    plt.ylim(-100,500)
    plt.show()
    

    st.pyplot(fig = plt.show())           
               
    
