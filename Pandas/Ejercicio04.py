import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)
print("Setup complete.")


#ejercicio 1
# Your code here
reviews_written = reviews.groupby('taster_twitter_handle').size()

# Check your answer
q1.check()

##########################################################
#ejercicio 2:
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

# Check your answer
q2.check()

##########################################################
#ejercicio 3:
price_extremes = reviews.groupby('variety')['price'].agg(['min', 'max'])

# Check your answer
q3.check()

##########################################################
#ejercicio 4:
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

# Check your answer
q4.check()

##########################################################
#ejercicio 5:
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()

# Check your answer
q5.check()

##########################################################
#ejercicio 6:
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

# Check your answer
q6.check()
