import tkinter as tk

import pandas as pd

import meal_tracker


# Gets user input and passes it to the search function
def search_button():
    search_results.delete("1.0", "end")
    search_input = row_input.get()
    column_input = radio_input.get()

    search_results.insert(tk.END, meal_tracker.search(column=column_input, query=search_input))


root = tk.Tk()
root.geometry("1500x700")
root.title("Meal Planner")

# Displays all data
all_data_text = tk.Text(root, height=30, width=70)
all_data_text.insert(tk.END, meal_tracker.get_data())

all_data_label = tk.StringVar()
all_data_label.set("All Meal Data")
adl = tk.Label(root, textvariable=all_data_label, height=2)

# Search bar + label
row_input = tk.StringVar()

search_label = tk.Label(root, text='Search Dataframe', font=('calibre', 10, 'bold'))

search_bar = tk.Entry(root, textvariable=row_input)

search_btn = tk.Button(root, text='Search', command=search_button)

# Search result textbox
search_results = tk.Text(root, height=20, width=70)

# Column selection
radio_input = tk.StringVar(root, "dish")

columns = {"Dish": "dish",
           "Difficulty": "difficulty",
           "Price": "price",
           "Tags": "tags"}

for (text, column) in columns.items():
    tk.Radiobutton(root, text=text, variable=radio_input,
                   value=column, background="light blue", indicatoron=False).pack(pady=5)


all_data_text.pack(side=tk.LEFT, padx=5)
adl.pack(side=tk.LEFT, pady=20)
search_label.pack()
search_bar.pack()
search_btn.pack()
search_results.pack()

tk.mainloop()
