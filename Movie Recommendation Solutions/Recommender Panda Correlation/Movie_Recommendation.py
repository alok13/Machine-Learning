import numpy as num
import pandas as pd
pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

## Observe data from Rating csv
rating_data=pd.read_csv("D:\CODING\Machine-Learning\Movie Recommendation Solutions\Movie_Recommender_2\ml-latest-small\ml-latest-small\\ratings.csv")
##print(rating_data.head())

## Observe data from Movie csv.
movie_name=pd.read_csv("D:\CODING\Machine-Learning\Movie Recommendation Solutions\Movie_Recommender_2\ml-latest-small\ml-latest-small\\movies.csv")
#print(movie_name.head())

## Merge both data frames to get ratings and movie names
movie_data=pd.merge(rating_data,movie_name,on='movieId')
#print(movie_data.head())

mean_rating=movie_data.groupby('title')['rating'].mean().sort_values(ascending=False)
#print(mean_rating.head())

number_of_rating=movie_data.groupby('title')['rating'].count().sort_values(ascending=False)
##print(number_of_rating.head())

## Sort the movies based on rating and count
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
#print(ratings_mean_count.head())
ratings_mean_count['rating_counts']=pd.DataFrame(movie_data.groupby('title')['rating'].count())

#print(ratings_mean_count.head())

## See the number of ratings on graph.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
'exec(%matplotlib inline)'

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor']=True
#ratings_mean_count['rating_counts'].hist(bins=50)

## See the average rating on graph
#ratings_mean_count['rating'].hist(bins=50)

##Plot average ratings vs no of rating counts
sns.jointplot(x='rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)
#plt.show()


user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')

forrest_gump_ratings = user_movie_rating['Forrest Gump (1994)']
#print(forrest_gump_ratings.head())

movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])
corr_forrest_gump.dropna(inplace=True)
#print(corr_forrest_gump.head())


sorted_answer=corr_forrest_gump.sort_values('Correlation', ascending=False).head(10)
#print(sorted_answer.head())

list_with_rating_count=corr_forrest_gump.join(ratings_mean_count['rating_counts'])
#print(list_with_rating_count.head())

final_result=list_with_rating_count[list_with_rating_count ['rating_counts']>50].sort_values('Correlation', ascending=False).head()
print(final_result.head())