import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(reviews)

print('\n select country from winesmag \n')
print(reviews.country)

print('\n sub dataset \n select country from winesmag \n')
reviews_country = reviews['country']
print(reviews_country)

print('\n country top 1 \n')
reviews_country_top1 = reviews['country'][2]
print(reviews_country_top1)

