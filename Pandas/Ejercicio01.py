import pandas as pd
pd.set_option('display.max_rows', 5)
print("Setup complete.")

# Ejercicio 1:
data = {'Apples': [30],
        'Bananas': [21]}

fruits = pd.DataFrame(data)

##########################################################
# Ejercicio 2:
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
        index=['2017 Sales', '2018 Sales'])


##########################################################
# Ejercicio 3:
data = {'Flour': '4 cups',
        'Milk': '1 cup',
        'Eggs': '2 large',
        'Spam': '1 can'}

ingredients = pd.Series(data, name='Dinner')


##########################################################
# Ejercicio 4:
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)


##########################################################
# Ejercicio 5:
animals.to_csv("cows_and_goats.csv")

