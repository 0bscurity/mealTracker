import pandas as pd
# import GUI


def get_data():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    imported_data = pd.read_csv('meal_data.csv')

    return imported_data


def search(column, query):
    df = get_data()

    column = column.capitalize()

    search_terms = query.split(",")
    search_terms = [x.strip(' ') for x in search_terms]

    query = [x for x in search_terms]

    matches = df.loc[(df[column].astype(str).str.contains('|'.join(query), case=False))]

    print(matches)
    return matches


# -------------------------- Command Line Code ----------------------------

def cli_search():
    df = get_data()

    print(df.columns.values)

    col_search_input = input("Enter column - ")
    row_search_input = input("Enter value(s) - ")

    search(col_search_input, row_search_input)


def cli_add():
    df = get_data()

    new_dish = {'dish': input("Dish - "),
                'difficulty': input("Difficulty - "),
                'price': input("Price - "),
                'tags': [input("Tags - ")],
                'Link': input("Link - ")
                }

    df.loc[len(df)] = new_dish

    print(df)


def edit():
    df = get_data()




def cli_startup():
    selection = input(f"\n* 1 - Search for a meal\n* 2 - Add a meal\n* 3 - Exit\n -- ")

    if selection == "1":
        cli_search()
        cli_startup()
    elif selection == "2":
        cli_add()
        cli_startup()
    elif selection == "3":
        exit()


cli_startup()
