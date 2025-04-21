import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered = animals[animals['weight'] > 100]
    sorted_animals = filtered.sort_values(by='weight', ascending=False)
    return sorted_animals[['name']]