import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#pd.set_option('display.max_columns', None)  
#pd.set_option('display.expand_frame_repr', False)
#pd.set_option('max_colwidth', -1)


##Read the csv
dataframe=pd.read_csv("movie_dataset.csv")

## See all the coloumns available
##print(dataframe.columns.values)

## Select the features that matters most
features =['keywords','cast','genres','director']

#filling all NaNs with blank string
for feature in features:
	dataframe[feature]=dataframe[feature].fillna('')

##Function to combine feature from a row
def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print ("Error:", row)	

## Calling combine_features method ober each row and adding in field
dataframe["combined_features"]=dataframe.apply(combine_features,axis=1)

#print("Combined Features:", dataframe["combined_features"].head())
#print(dataframe.iloc[0].combined_features)

# Create the count_matrix from combined_feature column
cv=CountVectorizer()
count_matrix=cv.fit_transform(dataframe["combined_features"])

#get cosine similarity 
cos_sim=cosine_similarity(count_matrix)

#helper functions
def get_title(index):
    return dataframe[dataframe.index == index]["title"].values[0]
def get_index(title):
    return dataframe[dataframe.title == title]["index"].values[0]

## TIME TO TEST

liked_movie="Gravity"

movie_index=get_index(liked_movie)

similar_movie = list(enumerate(cos_sim[movie_index]))

## Sort the movies in descending order
## Remove the first movie ,since its the movie itself
sorted_movies=sorted(similar_movie,key=lambda x:x[1],reverse=True)[1:]

#Print first 20 movies
i=0
for element in sorted_movies:
	print (get_title(element[0]))
	i=i+1
	if i>20:
		break



