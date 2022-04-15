import pandas as pd
#import GUI


def get_data():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    imported_data = pd.read_csv('meal_data.csv')

    return imported_data


def search(column, query):
    df = get_data()
    print(column, query)

    matches = df.loc[df[column].str.contains(query, case=False)]
    #matches = df.loc[df[column].isin([query])]
    #matches = df.loc[df[column] == query]

    print(matches)
    return matches


def add_dish():
    user_input = input("")


# Command Line
def cmd_search():
    df = get_data()

    print(df.columns.values)

    search_col = input("Enter search column - ")
    search_row = input("Enter search term - ")

    search(search_col, search_row)


def cmd_add():
    pass


selection = input(f"* 1 - Add a meal \n* 2 - Search for a meal\n* 3 - Exit\n -- ")

if selection == "1":
    cmd_add()
elif selection == "2":
    cmd_search()
elif selection == "3":
    exit()
