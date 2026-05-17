Updated: Fixed a typo from my first commit.

Note: Please see my email sent on May 17th at (it should be sent before 3AM).

IMDb Dataset:
I first loaded the two datasets, and for basics I only kept certain columns while tossing out the rest.
Next, I filtered to only keep entries from the 1990s, and that were only movies. Entries with missing
genre information were dropped. I next created a dictionary called movie_ratings, connecting movie id
to ratings, it works by looping through the ratings dataset, with the movie id being the key and the rating
being the value. This was done to make the script run faster. Originally I had a different method, but that 
one proved to be very slow so I changed to this. Next, I made an empty list called genre_data, which loops over
the entries in basics and gets the movie id and genres for each movie, and gets the ratings from the earlier
dictionary. Then, genres are paired with ratings, and appended to the list. Lastly, genre_data is turned into a
dataframe, then group by genres and calculate mean/median and sort values from highest to lowest. 

TMDb Dataset:
I first loaded the dataset. I converted release date to a datetime object, extracting it into release year while
invalid data is handled by errors=coerce. I then filtered the data to keep only entries from the 1990s. I had to
do some genre matching because the genre values in the csv were numbers, so I had to go find what genre each number
meant. After my research, I came back and made a dictionary that matches the numbers to their respective genres.
I then grabbed the average vote and genre ids into lists via tolist() for easy looping later, I came across tolist()
in my research. Next, I created an emtpy list called genre_data for genre-rating pair storing, then did a loop to get
the vote average and genre id. I used strip/replace/split to clean up the data. Next, I converted the genre_id into integers,
then the script checks if the id exists in the genre dictionary from earlier. Then I get the actual genre the number represents,
then append it to the list. I then make a dataframe from the genre-rating pairs, before doing the same group by genres and
calculating mean/median and sort values from highest to lowest.

For the graphing scripts, I imported the scripts from the other scripts, before importing seaborn and matplotlib. I called the
genre_ratings function from the respective scripts, before creating barplots to compare ratings between genres. I used title to
set a title for the plots and ylabel to name the y-axis, and used rotation to make the x-axis for graph 1 legible, as by default
the labels are all stacked on top of each other. 

Citations:

IMDb. (n.d.). IMDb Data Files Available for Download. https://datasets.imdbws.com/ ​



Nishad, A. (2025). TMDB Top Rated Movies with Genre and Metadata. Kaggle. https://www.kaggle.com/datasets/abhisheknishad8988/tmdb-top-rated-movies-with-genre-and-metadata ​

    Notes: I was unable to determine the day or month.​

    License Type: CC0

[ticao2 BR pt-BR]. (2019, October 23). Which Genre ID # is assigned to each movie category? [Online forum post]. TMDb. https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee#5db04e5fbfeb8b00131d823f 

    Notes: I was unsure what the group was. Also, the information I used came from a reply, not the main post.

