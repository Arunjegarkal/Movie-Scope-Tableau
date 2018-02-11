# Movie Scope Tableau

Dashboard link

https://arunjegarkal.github.io/Movie-Scope-Tableau/index.html


    Abstract    
In this paper we implement a system through which we can analyze and predict the box office collection of the movies. We build the system in such a way that people from various backgrounds can also interact with the system and the data we have. Through the interaction they can also find hidden trends and insights which some of us miss. The data contains various variables which are compiled from various sources. The data can be extremely exhaustive but we have tried to collect the information essential for the analysis of trends and insights.


    Introduction
    
Each year there are hundreds of movies which are released and being produced. The revenue of the movies depends on various factors like genre of the movie, critics review, quality of trailer, stardom of lead actor, studio of the movie being produced, director of the movie and various people included in movie making process. It can also depend on the current state of the economy, spending trends and habit of people, stock market and various other economic factors. The movie industry was worth more than 100 billion dollars in 2016[1]. And it is only expected to grow with number of new movies and stories and also the growing population. So it becomes useful to predict how much amount of money will one movie generate based on historic figures. In this paper we take into amount all the factors described above like genre, critics review, lead actor, studio etc. 

This demo helps to analyze and visualize the trends of the box office collection. End user can visualize the collections over the years based one the MPAA (Motion Picture Association of America) Rating's. Classify based on years, title name. Word cloud of top two movies help the user to know more about the movie summery, cast, genres. Review sentiment helps to know people opinion about the movie.
  
 FRAMEWORK AND METHODS
 
    Architecture
   
As show in Fig 1, We had collected data from IMDB and Movie DB and combined both the data set using unique id called imdbID into one data set and pre-processed to clean the data to make appropriate for analysis  and separated the dataset into text data and numerical data. Sentimental Analysis is performed on text data, used this sentimental results and numerical data to perform the analysis.

![architecture 1](https://user-images.githubusercontent.com/22176809/36079024-06aa3b9a-0f44-11e8-9092-3087e76c35f2.png)

fig 1 : Architecture of Trend Analyzer consist of different modules. Data Collection, Pre-Processing, Sentimental Analysis, Visualization/Dashboard each of these are explained in detail in further paper. 


       Data Collection
       
Data is collected from IMDB and The Movie Database(TMDB), IMDB crawler is built in python. “BeautifulSoap” is use to parse the HTML page and pull the necessary information. The information we get from the IMDB is less compared to the actual information of the movies. We would like to know the:Primary Language of movie,Production Companies,Budget of the movie,Overall Popularity of the movie, Revenue etc.These various information is collected from “The Movie Database”. Used unique movie id - "imdbID" from IMDB to get their corresponding information from Movie Database. We iterate through all the movies we obtained from the IMDB database.

Critics of movies explains in detail about the movie and gives the opinion of the movie either positive or negative which used for sentimental analysis. It would have been extremely difficult to collect all the reviews of all the critics as the data would have been too huge and we don't have the resources to compute any valuable information on it. So we considered only top 10 useful reviews and made the database of it for the demo purpose. 

    Pre-Processing

IMDB data contain information about some TV shows and plays which are not relevant to our analysis which are dropped from the data set. Release date of movies had Null, 0 or blank values we normalized to 0 indicating no release date available. Title filed had some non alphanumeric characters removed those characters.

    Sentimental Analysis

After data collection, we pre-proceed the data by removing the special characters and stop words, tokenized the reviews and tag each token with Part of Speech(POS) such as adjective, verb and adverb which helps in determining the sentiment of each review. Then we be trained 6 machine learning algorithms i.e. Naive Bayes, MultinomialNB , BernoulliNB, SVC , LinearSVC and NuSVC  and applied it to test data for predicting the sentiment of reviews. We then compared each of the classifier’s result with voting algorithm to measure the confidence about the correctness of sentiment prediction. Used this sentiments for comparing the critics review with box office collection.

Demonstration

    Features
Our System is capable of answering various queries of movies trends, annual box office collection, Annual Movie Releases, User opinion of the movie in terms of sentiment ratio and Word Cloud describing movie like cast,brief summery about movie, genres below fig show the dashboard of our system.

![fig3 2](https://user-images.githubusercontent.com/22176809/36079104-191f0e3a-0f45-11e8-8f73-4bb530e201c6.PNG)
fig 2 : Dashboard 1)Movie Release per Year 2)Box Office collection per Year 3)Word cloud about the movie 4)Box Office collection per Rating 5)Movie released per Rating 6)Sentimental Analysis of Reviews 7)Filters based on Year and Movie Title 8) Color code assigned for each rating

    Visualization
    
Fig 2. Our system consist of 6 charts and graphs each gives different information 1) Movie Release per Year : there is always increase in number of movie release per year except there bit decrease in year 2009 to 2011 because in those years there was a financial break down same caused the decrease in box office collection in those year we can observe that in 2) Box Office collection per Year 3) Word cloud gives the brief information like summary, cast, genre of top two  movies in 2016. 4) Box Office collection per MPAA Rating 5) Movie released per Rating. From char 4 Collection of PG-13 rated movies are compared to R rated movies even though the number of movies released are less. Chart 6) show the ratio of Sentimental Analysis of Reviews. Also provides the user an option to see trends based on year and movie names. In fig 2 we can observe that there drastic increase in number of movies release's every year specially PG-13 rated movies.

    Case Study
    
There is increase in box office collection every year and positive reviews are declined over the years. The Production Budget has increased overall. There are more number of R-rated movies, however PG-13 brings in more revenue. There is a dip in box office collection in 2008, 2009, 2010 corresponds to Financial Depression of 2008.

    Experimental Result
    
There is increase in box office collection every year and positive reviews are declined over the years. The Production Budget has increased overall. There are more number of R-rated movies, however PG-13 brings in more revenue. There is a dip in box office collection in 2008, 2009, 2010 corresponds to Financial Depression of 2008.

    Conclusions
    
We attempt to create a system where people can interact with the data we have provided. Along with the fun they can also find various trends in box office collection and also predict some of the hidden trends in box office collection. The data provided by us is built by assimilating data from various sources and helps in analyzing those trends.  


