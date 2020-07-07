import pandas as pd
from matplotlib.patches import Arc, Circle, Rectangle

import matplotlib.pyplot as plt

from scipy import spatial




## http://savvastjortjoglou.com/nba-shot-sharts.html

### code to draw nba court

def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                          fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                          fill=False)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                               color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                    color=color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax





## code to convert all of the X,Y shots into my different shooting zones

# dataframe needs to be in the format of the shot chart data that is provided by the nba api

def shooting_positions(df):
    left_corner_3 = df.loc[(df.LOC_X > -250) & (df.LOC_X <= -220) & (df.LOC_Y <= 87)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'left_corner_3'})

    right_corner_3 = df.loc[(df.LOC_X > 220) & (df.LOC_X <= 250) & (df.LOC_Y <= 87)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'right_corner_3'})

    left_wing_3 = df.loc[(df.LOC_X > -250) & (df.LOC_X <= -80) & (df.LOC_Y > 87) & (df.LOC_Y <= 280) & (
                df.SHOT_ZONE_BASIC == 'Above the Break 3')].groupby('PLAYER_NAME')['LOC_X'].count().to_frame().rename(
        columns={'LOC_X': 'left_wing_3'})

    right_wing_3 = df.loc[(df.LOC_X > 80) & (df.LOC_X <= 250) & (df.LOC_Y > 87) & (df.LOC_Y <= 280) & (
                df.SHOT_ZONE_BASIC == 'Above the Break 3')].groupby('PLAYER_NAME')['LOC_X'].count().to_frame().rename(
        columns={'LOC_X': 'right_wing_3'})

    center_3 = df.loc[(df.LOC_X > -80) & (df.LOC_X <= 80) & (df.LOC_Y > 87) & (df.LOC_Y <= 280) & (
                df.SHOT_ZONE_BASIC == 'Above the Break 3')].groupby('PLAYER_NAME')['LOC_X'].count().to_frame().rename(
        columns={'LOC_X': 'center_3'})

    deep_3 = df.loc[(df.LOC_Y > 280) & (df.LOC_Y <= 350)].groupby('PLAYER_NAME')['LOC_X'].count().to_frame().rename(
        columns={'LOC_X': 'deep_3'})

    heave = df.loc[(df.LOC_Y > 350)].groupby('PLAYER_NAME')['LOC_X'].count().to_frame().rename(
        columns={'LOC_X': 'heave'})

    left_baseline_deep_2 = df.loc[(df.LOC_X > -220) & (df.LOC_X <= -150) & (df.LOC_Y <= 87)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'left_baseline_deep_2'})

    right_baseline_deep_2 = df.loc[(df.LOC_X > 150) & (df.LOC_X <= 220) & (df.LOC_Y <= 87)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'right_baseline_deep_2'})

    left_wing_deep_2 = df.loc[((df.LOC_X > -220) & (df.LOC_X <= -150) & (df.LOC_Y > 87)) | (
                ((df.LOC_X > -150) & (df.LOC_X <= -80) & (df.LOC_Y > 150)) & (
                    df.SHOT_ZONE_BASIC == 'Mid-Range'))].groupby('PLAYER_NAME')['LOC_X'].count().to_frame().rename(
        columns={'LOC_X': 'left_wing_deep_2'})

    right_wing_deep_2 = df.loc[(((df.LOC_X > 150) & (df.LOC_X <= 220) & (df.LOC_Y > 87)) | (
                (df.LOC_X > 800) & (df.LOC_X <= 150) & (df.LOC_Y > 150))) & (
                                           df.SHOT_ZONE_BASIC == 'Mid-Range')].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'right_wing_deep_2'})

    left_baseline_short_2 = df.loc[(df.LOC_X > -150) & (df.LOC_X <= -80) & (df.LOC_Y <= 87)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'left_baseline_short_2'})

    right_baseline_short_2 = df.loc[(df.LOC_X > 80) & (df.LOC_X <= 150) & (df.LOC_Y <= 87)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'right_baseline_short_2'})

    left_wing_short_2 = \
    df.loc[(df.LOC_X > -150) & (df.LOC_X <= -80) & (df.LOC_Y > 87) & (df.LOC_Y <= 150)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'left_wing_short_2'})

    right_wing_short_2 = \
    df.loc[(df.LOC_X > 80) & (df.LOC_X <= 150) & (df.LOC_Y > 87) & (df.LOC_Y <= 150)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'right_wing_short_2'})

    deep_center_2 = \
    df.loc[(df.LOC_X > -80) & (df.LOC_X <= 80) & (df.LOC_Y > 210) & (df.SHOT_ZONE_BASIC == 'Mid-Range')].groupby(
        'PLAYER_NAME')['LOC_X'].count().to_frame().rename(columns={'LOC_X': 'deep_center_2'})

    short_center_2 = \
    df.loc[(df.LOC_X > -80) & (df.LOC_X <= 80) & (df.LOC_Y > 150) & (df.LOC_Y <= 210)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'short_center_2'})

    floater_range = \
    df.loc[(df.LOC_X > -80) & (df.LOC_X <= 80) & (df.LOC_Y > 87) & (df.LOC_Y <= 150)].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'floater_range'})

    in_the_paint = df.loc[(df.LOC_X > -80) & (df.LOC_X <= 80) & (df.LOC_Y <= 87) & (
                df.SHOT_ZONE_BASIC == 'In The Paint (Non-RA)')].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'in_the_paint'})

    restricted_area = df.loc[(df.SHOT_ZONE_BASIC == 'Restricted Area')].groupby('PLAYER_NAME')[
        'LOC_X'].count().to_frame().rename(columns={'LOC_X': 'restricted_area'})

    return left_corner_3, right_corner_3, left_wing_3, right_wing_3, center_3, deep_3, heave, left_baseline_deep_2, right_baseline_deep_2, left_wing_deep_2, right_wing_deep_2, left_baseline_short_2, right_baseline_short_2, left_wing_short_2, right_wing_short_2, deep_center_2, short_center_2, floater_range, in_the_paint, restricted_area






# function to go through all of the players, and find the most similar player to them using euclidean distance

def similarity(features, df):
    
    #creates a dictionary to store all the results
    similarities = {}

    #first the outer loop to go through all of the players
    for i in range(0, len(df)):
        
        # initializing a random best similarity since we want to find the smallest number we use this as the initial
        best_similarity = 1000000

        # second loop to go through the players again
        for j in range(0, len(df)):
            
            # make sure the same player doesnt match with himself as the similarity distance is 0
            if i != j:
                
                # Finding the similarity score for each combination of players
                similarity = spatial.distance.euclidean(features.iloc[i], features.iloc[j])

                # if the score is lower then the previous it resets and saves that index
                if similarity < best_similarity:
                    
                    # change the new best similarity
                    best_similarity = similarity
                    
                    # save the index of that similarity
                    holder = j

        # store the player with his most comparable player
        similarities[df.iloc[i].Player] = df.iloc[holder].Player
        
    return similarities