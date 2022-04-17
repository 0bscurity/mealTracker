import pandas as pd
# import GUI

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def get_data():
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


def add():
    df = get_data()

    new_dish = {'Dish': input("Dish - "),
                'Difficulty': input("Difficulty - "),
                'Price': input("Price - "),
                'Tags': [input("Tags - ")],
                'Link': input("Link - ")
                }

    df.loc[len(df)] = new_dish
    df.to_csv('meal_data.csv', index=False)
    print(df)


def edit():
    df = get_data()

    dish_name = input(f"Enter the meal you wish to edit\n -- ")

    search("Dish", dish_name)

    index = df.index[df["Dish"].astype(str).str.contains(dish_name)].tolist()

    # if len(index) > 1:
    #     selection = input(f"There are more than one '{dish_name}'\nPlease type full dish name\n -- ")
    #     index = df.index[df["Dish"].astype(str).str.contains(selection)].tolist()

    column = input(f"Which column would you like to edit?\n -- ").capitalize()
    replacement = input(f"What would you like the new value to be?\n -- ")

    print(index)
    df.loc[index, column] = replacement
    df.to_csv('meal_data.csv', index=False)


def delete():
    df = get_data()

    dish_name = input(f"Enter the meal you wish to delete\n -- ")

    search("Dish", dish_name)

    index = df.index[df["Dish"].astype(str).str.contains(dish_name)].tolist()

    confirmation = input(f"Are you sure you want to delete {dish_name}? (y/n)\n -- ")

    if confirmation == "y":
        df = df.drop(index)
        df.to_csv('meal_data.csv', index=False)
        print(f"Meal deleted")
    else:
        startup()


# Recursion galore startup menu
def startup():
    selection = input(f"\n* 1 - Search for a meal\n* 2 - Add a meal\n* 3 - Edit a meal\n* 4 - Remove a meal\n"
                      f"* 5 - Exit\n -- ")

    if selection == "1":
        cli_search()
        startup()
    elif selection == "2":
        add()
        startup()
    elif selection == "3":
        edit()
        startup()
    elif selection == "4":
        delete()
        startup()
    elif selection == "5":
        exit()


startup()
