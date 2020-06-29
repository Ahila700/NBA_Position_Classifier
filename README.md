# NBA_Position_Classifier

### Classifying nba players by position is simple enough, taller players who get rebounds are centers, smaller players who get assists are point guards. But if you take size out of the equation, how good will it be? Well thats what im trying to figure out. The 5 positions themselves have been defined since the game started, with rare exceptions. But now i want to take the skill aspect, the shooting position of players, points, rebounds, assists, etc without any of the physical measurements and classify players. I started with the idea of using the generally defined 5 positions as the classes but as i went along and ran models, as well as thought more about it with the way the modern nba is played i found that actually a 3 class classification makes more sense. The reason is that power forwards and centers (the 2 big man positions) operate in very similar ways from where they shoot from to the high rebounds and blocks. and small forwards and shooting guards in the nba have become very malleable now a days and thinking back the only thing that made someone a shooting guard vs a small forward was if they were 6'7" or shorter/taller depending on position. So in my new model i decided to go with 3 classes, Point guards, who are very distinct in style, shooting guards and centers.

### Obviously the point of the classification model is to achieve a high accuracy but i had another idea in mind as well, what if my model is wrong, but its wrong because a player is just classified poorly. Well thats what i hope to achieve, i want a good model not based solely on how well it scores but how well it classifies players by their style of play. So someone like LeBron James who has constantly been the facilitator for his teams since he came into the league in 2003 should be classified as a Point guard even though he is 6'8" and 280 pounds. Thats what i want out of the model and the biggest goal of the presentation.

### So to do this i used 2 main things from the nba api and basketball reference page. The shooting locations over a 20 year span which can be obtained through the nba api. And the yearly per game averages of the players obtained through the basketball reference pages. These along with a ton of feature engineering are the biggest factors in the modeling. (more to come in the future including defensive statistics)

## Breakdown of the files

- Images: Collection of all the images gathered through eda including nba player shot charts and breakdown of the shot distribution over the years

![](Images/harden.png)

![](Images/Shooting_by_year.png)

- CSV Files: Collection of all the CSV files gathered throughout the entire data gathering, data cleaning and feature creation processes

- mod_5_functions: python file with the large functions that were used in the notebooks. meant to keep the notebooks themselves much clearner and be able to slim down the large notebooks

- nba_data_gathering notebook: gathering all the available data from the nba_api. Gathered shot charts from 2000 to 2020 but because the file was too large to include in the github i added a smaller file with shot charts from just the last season, this can be used as a replacement to run all the code 

- bbref_data_gathering notebook: gathering the player bios for the last 20 years, this include points, rebounds, assists, field goal %, etc

- Defensive stats and shot charts notebooks: these both served the same purpose. to take the data from the nba api and be able to convert it to values that could be used in a model in the future. You can see my breakdown of the court below as well as the breakdown of the values for each shot location

![](Images/nba_court.png)

![](Images/download%20(1).png)

- Modeling and EDA notebook: The final notebook, this has all of the EDA analysis, shot charts, shot value graphs, etc meant to get an idea of the features and be able to clean them up further if necessary. Also has all of the models for both 3 and 5 class models, including dummy classifier, XGBoost classifier, random forest classifier and support vector machine classifier and an analysis of the results using feature coefficients and confusion matrices

![](Images/feature_importance_all.png)

![](Images/rf_5_class.png)




## Citations

- http://savvastjortjoglou.com/nba-shot-sharts.html
  - used to create nba court to map the data i have 
  
- https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
  - code to find the most common word in a string (just done to simplify the work)

- https://stackoverflow.com/questions/41592661/determining-the-most-contributing-features-for-svm-classifier-in-sklearn
  - code to find the feature importance of svm models
  
- https://www.123rf.com/photo_9886489_basketball-sequences.html
- https://www.ppt-backgrounds.net/basketball/8193-basketball--basketball-court-wood---presentation-background-backgrounds.html
- https://basketballphantom.com/position-play-basketball/
  - images used in presentation
