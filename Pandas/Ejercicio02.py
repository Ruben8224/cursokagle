# Ejercicio 1:
# Your code here
desc = reviews['description']

# Check your answer
q1.check()


##########################################################
# Ejercicio 2:
first_description = reviews.loc[0, 'description']

# Check your answer
q2.check()
first_description


##########################################################
# Ejercicio 3:
first_row = reviews.loc[0]

# Check your answer
q3.check()
first_row

##########################################################
# Ejercicio 4:
first_descriptions = reviews['description'].head(10)


# Check your answer
q4.check()
first_descriptions

##########################################################
# Ejercicio 5:
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]


# Check your answer
q5.check()
sample_reviews

##########################################################
# Ejercicio 6:
df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]


# Check your answer
q6.check()
df

##########################################################
# Ejercicio 7:
df = reviews.loc[:99, ['country', 'variety']]

# Check your answer
q7.check()
df

##########################################################
# Ejercicio 8:
italian_wines = reviews[reviews['country'] == 'Italy']


# Check your answer
q8.check()

##########################################################
# Ejercicio 9:
top_oceania_wines = reviews[(reviews['points'] >= 95) & ((reviews['country'] == 'Australia') | (reviews['country'] == 'New Zealand'))]


# Check your answer
q9.check()
top_oceania_wines