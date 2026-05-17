from IS362_Final2 import genre_ratings
import seaborn as sns
import matplotlib.pyplot as plt

genre_means, genre_medians = genre_ratings()

sns.barplot(x=genre_means.index, y=genre_means.values)
plt.title("Genre Means (TMDb)")
plt.ylabel("Ratings")
plt.show()