import pandas as pd
import GUI


def get_data():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    imported_data = pd.read_csv('meal_data.csv')

    return imported_data


def search(column, query):
    df = get_data()

    matches = df.loc[df[column].str.contains(query, case=False)]

    print(matches)
    return matches


def add_dish():
    user_input = input("")
