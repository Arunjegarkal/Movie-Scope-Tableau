# Movie Scope Tableau

    Abstract    
In this paper we implement a system through which we can analyze and predict the box office collection of the movies. We build the system in such a way that people from various backgrounds can also interact with the system and the data we have. Through the interaction they can also find hidden trends and insights which some of us miss. The data contains various variables which are compiled from various sources. The data can be extremely exhaustive but we have tried to collect the information essential for the analysis of trends and insights.


    Introduction
    
The movies and plays are one of the most important form of art and as well as entertainment. Each year there are hundreds of movies which are released and being produced. The revenue of the movies depends on various factors like genre of the movie, critics review, quality of trailer, stardom of lead actor, studio of the movie being produced, director of the movie and various people included in movie making process. It can also depend on the current state of the economy, spending trends and habit of people, stock market and various other economic factors. 

The movie industry was worth more than 100 billion dollars in 2016[1]. And it is only expected to grow with number of new movies and stories and also the growing population. So it becomes useful to predict how much amount of money will one movie generate based on historic figures. In this paper we take into amount various factors like genre of the movie, critics review, quality of trailer, stardom of lead actor, studio of the movie being produced, director of the movie and various people included in movie making process, current state of the economy, spending trends  etc. 

In this paper we try to analyze the trends of the box office and also provide tools for other interested researcher to analyze the data-set. 

We can get the data of 5000 movies from popular data-mining challenges website kaggle[2]. However for this project we decided to build our own data-set. The data set built contains the information of over 12,500 movies from 1976-2016. We use couple of websites from which we gather the data. We use IMDB and The Movie DB to build our data-set.

We try to leverage the information from both these sites to build our data-set. We select the necessary variables like year , name , rating, genre, production companies, revenue, budget, votes, popularity etc from both these sites. 

    Architecture
   
One of the challenges to build the data set is that, the data sources are spread over many places, we need to identify, collect and consolidate the data sources to build the data set to our need and specification. We used IMDB and The Movie Database(TMDB) to build our database. We grab the data from the home page of IMDB, we grab Movie Name, year, Rating, Revenue from the IMDB page for each movies released in year from 1976 to 2016. We also store the IMDB-id from the IMDB page which will later be used to consolidate data from various source. 

We then use TMDB-API to collect extra information about the movie. We collect information like Primary Language of movie, Production Companies of each movie using imdbid. We then combine these two data sources to buid the data source. The architecture of the data collection is shown in fig 1.
