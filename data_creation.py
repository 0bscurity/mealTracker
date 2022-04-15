import random
import pandas as pd
from faker import Faker

fake = Faker()
the_list = []

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

tags = ['tag1', 'tag2']
for _ in range(100):
    dataset = {'Dish': fake.name(),
               'Difficulty': random.randrange(1, 10),
               'Price': random.randrange(3, 30),
               'Tags': tags,
               'Link': fake.company_email(),
               }

    dataset_copy = dataset.copy()

    the_list.append(dataset_copy)

df = pd.DataFrame(the_list)
print(df)

df.to_csv('meal_data.csv', index=True)
