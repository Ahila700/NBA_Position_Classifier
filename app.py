import streamlit as st
import pandas as pd
import numpy as np

import pickle
from pickle import load

from mod_5_functions import draw_court

import matplotlib.pyplot as plt

from matplotlib.patches import Arc, Circle, Rectangle

import re
import string

import warnings
warnings.filterwarnings('ignore')



st.title("NBA Position Classifier")
st.markdown("This application is a Streamlit dashboard that can be used to check the new position of a modern NBA player as "
            "well as the most similar player to him in the league. Just enter his name below (If there is any punctuation"  
            " in the players name, replace it with nothing exs: P.J. Tucker -> PJ Tucker, Shai Gilgeous-Alexander -> Shai GilgeousAlexander):")

 
# importing csv file
df = pd.read_csv('csv_files/Player_comparison_wo_defense_df.csv', index_col = 0)

# importing csv file for shot charts
shot_charts = pd.read_csv('csv_files/2019-20_nba_shot_charts.csv', index_col = 0)

## Have to clean the names on the shot_charts to what i cleaned the ones on the df file. 


def clean_names(name):
    name = re.sub('[%s]' % re.escape(string.punctuation), '', name)
    name = re.sub('ć', 'c', name)
    name = re.sub('Ć', 'C', name)
    name = re.sub('Ž', 'Z', name)
    name = re.sub('č', 'c', name)
    name = re.sub('Č', 'C', name)
    return name

# creating an object that applys the cleaning function to all of the rows of a column instead of on the column
cleaning = lambda x: clean_names(x)

shot_charts['PLAYER_NAME'] = pd.DataFrame(shot_charts.PLAYER_NAME.apply(cleaning))


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
               
    
