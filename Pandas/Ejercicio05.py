#ejercicio 1
# Your code here
dtype = reviews['points'].dtype

# Check your answer
q1.check()

##########################################################
#ejercicio 2
point_strings = reviews['points'].astype(str)

# Check your answer
q2.check()

##########################################################
#ejercicio 3
n_missing_prices = reviews['price'].isnull().sum()

# Check your answer
q3.check()

##########################################################
#ejercicio 4
reviews_per_region = reviews['region_1'].fillna('Unknown').value_counts().sort_values(ascending=False)

# Check your answer
q4.check()
