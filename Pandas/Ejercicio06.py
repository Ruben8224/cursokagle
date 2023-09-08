import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print("Setup complete.")

#ejercicio 1:
# Your code here
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})

# Check your answer
q1.check()

##########################################################
#ejercicio 2:
reindexed = reviews.rename_axis('wines', axis='rows')

# Check your answer
q2.check()
##########################################################
#ejercicio 3:
import pandas as pd

# Load the gaming products DataFrame
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"

# Load the movie products DataFrame
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

# Combine the gaming and movie products DataFrames
combined_products = pd.concat([gaming_products, movie_products])

# Check your answer
q3.check()

##########################################################
#ejercicio 4:
import pandas as pd
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))

# Check your answer
q4.check()