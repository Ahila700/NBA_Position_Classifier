# NBA Position Classifier


## Project Overview

Classifying nba players by position is simple enough, taller players who get rebounds are centers, smaller players who get assists are point guards. But if you take size out of the equation, how good will it be? Well thats what im trying to figure out. The 5 positions themselves have been defined since the game started, with rare exceptions. But now i want to take the skill aspect, the shooting position of players, points, rebounds, assists, etc without any of the physical measurements and classify players. I started with the idea of using the generally defined 5 positions as the classes but as i went along and ran models, as well as thought more about it with the way the modern nba is played i found that actually a 3 class classification makes more sense. The reason is that power forwards and centers (the 2 big man positions) operate in very similar ways from where they shoot from to the high rebounds and blocks. and small forwards and shooting guards in the nba have become very malleable now a days and thinking back the only thing that made someone a shooting guard vs a small forward was if they were 6'7" or shorter/taller depending on position. So in my new model i decided to go with 3 classes, Point guards, who are very distinct in style, shooting guards and centers.

Obviously the point of the classification model is to achieve a high accuracy but i had another idea in mind as well, what if my model is wrong, but its wrong because a player is just classified poorly. Well thats what i hope to achieve, i want a good model not based solely on how well it scores but how well it classifies players by their style of play. So someone like Dirk Nowitzki who shoots like a wing is classified as such and its important to know that when building a team around him. Because even if he is a big since he plays like a wing you need another big to complement him.

So now that the classification was done i wanted to look at using these same stats to compare players regardless of position. The reason for this is that some players fit very well with a team and because contracts generally don’t run much longer than 2 or 3 years being able to find similar players is really important for teams to build every year and maintain continuity with their style.

So using euclidean distance as a measure of similarity i found the most similar player for every player in the dataset. I want to note that I only used the 2019/20 season for this because I wanted this to be for active nba players only so that current teams could be able to use this. 

 
 
## Process and Data Gathering

So to do this i used 2 main things from the nba api and basketball reference page. The shooting locations over a 20 year span which can be obtained through the nba api. And the yearly per game averages of the players obtained through the basketball reference pages. These along with a ton of feature engineering are the biggest factors in the modeling. (more to come in the future including defensive statistics).

I got 650k+ shots for about 2000 nba players over the last 2 decades as well as their yearly per game stats,

## Github Repo Content

- Images: Collection of all the images gathered through eda including nba player shot charts and breakdown of the shot distribution over the years

![](Images/harden.png)

![](Images/Shooting_by_year.png)

- CSV Files: Collection of all the CSV files gathered throughout the entire data gathering, data cleaning and feature creation processes

- mod_5_functions: python file with the large functions that were used in the notebooks. meant to keep the notebooks themselves much clearner and be able to slim down the large notebooks

- Player Classification data gather - combination of all the data gathering and cleaning in the project for the classification modeling. This includes, gathering shot chart data through the nba api, scraping data from basketball reference, and cleaning and merging the data between those 2 sites for use in the final modeling.

![](Images/nba_court.png)

![](Images/download%20(1).png)

- Modeling and EDA notebook: The final notebook, this has all of the EDA analysis, shot charts, shot value graphs, etc meant to get an idea of the features and be able to clean them up further if necessary. Also has all of the models for both 3 and 5 class models, including dummy classifier, XGBoost classifier, random forest classifier and support vector machine classifier and an analysis of the results using feature coefficients and confusion matrices

![](Images/feature_importance_all.png)

![](Images/rf_5_class.png)

- Player Comparison data gather - combination of all the data gathering and cleaning in the project for the comparison modeling. This includes, gathering shot chart and defensive data through the nba api, scraping data from basketball reference, and cleaning and merging the data between those 2 sites for use in the final modeling.

- Player comparison modeling - In the end the defensive stats ended up doing less to help than harm the data. Because the defensive tracking data is not that new it cut down the player base from 500 to less than 300 and because of this it ended up being left out of the final model. Similarity score was used, with euclidean distance as that gave the best results to compare players.

![](Images/Harden_Doncic_shot_comparison.png)

- App (Streamlit) - Front-end local site to use to be able to input a player name (has to be entered properly) and output their classified position, the most similar player and the comparison of the shot charts between them and the most similar player to see why that player was chosen.

## Reproduction instructions

The all notebooks can be run top to bottom as they are. 

To completely reproduce the data, it must first start with the data gathering and cleaning which can be run from top to bottom. And then the modeling for classification and comparison can be run afterwards. 

## Conclusion

The best model was a support vector machine that got about an 85% accuracy and did well with the f1 score as well. So the skill set of players does a relatively good job in classifying the players but the best aspect as I mentioned in the intro was for players like Dirk Nowitzki who is a big but got classified as a wing because of his diverse shooting profile. These are the players who I was most curious about because even though Dirk is classified as a big because of his skill set it is very important to use him like a wing and build around him like a wing. And thats what the Mavericks did in summer of 2010 signing another big in Tyson chandler who has the skill set of a big and that complementary skill was a big part of why the Mavericks won the championship in that same season. This is what i want to get out of the classifier to be able to input a player and output their actual position based on skill.

## Future Steps

One big thing I would like to improve on is to weigh the different seasons as we get further away from the present. One of the worries I had going in was that the game has changed over time. So giving more weight to shot selection of players from 2010-2020 in the model as opposed to 2000-2010 would, in my opinion, give the model more accuracy. 



## Presentation Link

https://docs.google.com/presentation/d/1DMR6XEHKJiMgS-UF0zZWL_KOSlFBALFC0YeXH5uleaI/edit?usp=sharing

## Medium Article

https://antoniohila.medium.com/nba-player-comparison-and-position-classifier-85094a3ef9f

## Citations

- http://savvastjortjoglou.com/nba-shot-sharts.html
  - used to create nba court to map the data i have 
  
- https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
  - code to find the most common word in a string (just done to simplify the work)

- https://stackoverflow.com/questions/44511636/matplotlib-plot-feature-importance-with-feature-names/49157712
  - code to find the feature importance of svm models
  
- https://www.123rf.com/photo_9886489_basketball-sequences.html
- https://www.ppt-backgrounds.net/basketball/8193-basketball--basketball-court-wood---presentation-background-backgrounds.html
- https://basketballphantom.com/position-play-basketball/
  - images used in presentation
