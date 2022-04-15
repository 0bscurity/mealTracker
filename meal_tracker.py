import pandas as pd
#import GUI


def get_data():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    imported_data = pd.read_csv('meal_data.csv')

    return imported_data


def search(query):
    df = get_data()

    search_terms = query.split(",")
    search_terms = [x.strip(' ') for x in search_terms]

    column = search_terms[0]
    query = [x for x in search_terms[1:]]

    matches = df.loc[(df[column].astype(str).str.contains('|'.join(query), case=False))]

    print(matches)
    return matches


def add_dish():
    user_input = input("")


# -------------------------- Command Line Code ----------------------------

def cmd_search():
    df = get_data()

    print(df.columns.values)

    search_input = input("Enter search terms [column, value(s)] - ")

    search(search_input)


def cmd_add():
    df = get_data()

    new_dish = []

    columns = df.columns.values

    for column in columns:
        user_input = input(f"{column} - ")
        user_input = user_input.split(",")
        user_input = [x.strip(' ') for x in user_input]
        new_dish.append(user_input)

    print(new_dish)


def startup_options():
    selection = input(f"\n* 1 - Search for a meal\n* 2 - Add a meal\n* 3 - Exit\n -- ")

    if selection == "1":
        cmd_search()
        startup_options()
    elif selection == "2":
        cmd_add()
        startup_options()
    elif selection == "3":
        exit()

startup_options()
