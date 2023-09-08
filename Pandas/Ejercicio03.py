import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print("Setup complete.")

# Ejercicio 1:
median_points = reviews['points'].median()

# Check your answer
q1.check()

##########################################################
# Ejercicio 2:
countries = reviews['country'].unique()

# Check your answer
q2.check()

##########################################################
# Ejercicio 3:
reviews_per_country = reviews['country'].value_counts()

# Check your answer
q3.check()

##########################################################
# Ejercicio 4:
centered_price = reviews['price'] - reviews['price'].mean()

# Check your answer
q4.check()

##########################################################
# Ejercicio 5:
bargain_wine = reviews.loc[(reviews['points'] / reviews['price']).idxmax(), 'title']

# Check your answer
q5.check()

##########################################################
# Ejercicio 6:
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

# Check your answer
q6.check()

##########################################################
#ejercicio 7:
def get_star_rating(row):
    if row['country'] == 'Canada':
        return 3
    elif row['points'] >= 95:
        return 3
    elif row['points'] >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(get_star_rating, axis=1)


# Check your answer
q7.check()