import pandas as pd

def genre_ratings():
    basics = pd.read_csv("title.basics.tsv", sep="\t", na_values="\\N", usecols=["tconst", "titleType", "startYear", "genres"])

    ratings = pd.read_csv("title.ratings.tsv", sep="\t", na_values="\\N")

    basics["startYear"] = pd.to_numeric(basics["startYear"], errors="coerce")

    basics = basics[(basics["startYear"] >= 1990) & (basics["startYear"] <= 1999) & (basics["titleType"] == "movie")]

    basics = basics[basics["genres"].notna()]

    movie_ratings = {}
    
    for row_index_ratings in range(len(ratings)):
        tconst = ratings.iloc[row_index_ratings]["tconst"]
        rating = ratings.iloc[row_index_ratings]["averageRating"]
        movie_ratings[tconst] = rating

    genre_data = []

    for row_index_basics in range(len(basics)):
        tconst = basics.iloc[row_index_basics]["tconst"]
        genres = basics.iloc[row_index_basics]["genres"]

        if tconst not in movie_ratings:
            continue

        rating = movie_ratings[tconst]

        for genre in genres.split(","):
            genre_data.append([genre, rating])

    dataframe_1 = pd.DataFrame(genre_data, columns=["genres", "averageRating"])

    genre_means = dataframe_1.groupby("genres")["averageRating"].mean().sort_values(ascending=False)
    print("Mean per genre:\n", genre_means, "\n")

    genre_medians = dataframe_1.groupby("genres")["averageRating"].median().sort_values(ascending=False)
    print("Median per genre:\n", genre_medians, "\n")

    return genre_means, genre_medians

if __name__ == "__main__":
    genre_ratings()