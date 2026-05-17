import pandas as pd

def genre_ratings():
    tmdb = pd.read_csv("tmdb_2025.csv")

    tmdb["release_year"] = pd.to_datetime(tmdb["release_date"], errors="coerce", format="%d-%m-%Y").dt.year

    tmdb_90s = tmdb[(tmdb["release_year"] >= 1990) & (tmdb["release_year"] <= 1999)]

    genre_match = {
        28: "Action", 
        12: "Adventure", 
        16: "Animation", 
        35: "Comedy",
        80: "Crime", 
        99: "Documentary", 
        18: "Drama", 
        10751: "Family",
        14: "Fantasy", 
        36: "History", 
        27: "Horror", 
        10402: "Music",
        9648: "Mystery", 
        10749: "Romance", 
        878: "Science Fiction",
        10770: "TV Movie", 
        53: "Thriller", 
        10752: "War", 
        37: "Western"
    }

    ratings = tmdb_90s["vote_average"].tolist()
    genres_id_entries = tmdb_90s["genre_ids"].tolist()

    genre_data = []

    for row_index in range(len(ratings)):
        rating = ratings[row_index]
        genres_str = genres_id_entries[row_index]

        if type(genres_str) != str:
            continue

        genre_ids = genres_str.strip("[]").replace(" ", "").split(",")

        for genre_id in genre_ids:
            genre_id_int = int(genre_id)
            if genre_id_int in genre_match:
                genre_name = genre_match[genre_id_int]
                genre_data.append([genre_name, rating])

    dataframe_2 = pd.DataFrame(genre_data, columns=["genres", "vote_average"])

    genre_means = dataframe_2.groupby("genres")["vote_average"].mean().sort_values(ascending=False)
    print("Mean per genre:\n", genre_means, "\n")

    genre_medians = dataframe_2.groupby("genres")["vote_average"].median().sort_values(ascending=False)
    print("Median per genre:\n", genre_medians, "\n")

    return genre_means, genre_medians

if __name__ == "__main__":
    genre_ratings()