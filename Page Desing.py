import tkinter as tk
from tkinter import messagebox

library = [
    {"title": "RAMAYANA", "author": "VALMIKI MAHARSHI"},
    {"title": "MAHA BHARATHAM", "author": "VYASA"},
    {"title": "BAGAVATHAM", "author": "VEDA VYASA"},
    {"title": "TOM SAWYER", "author": "MARK TWAIN"},
    {"title": "GITHANJALI", "author": "RABINDRANATH TAGORE"}
]

def search_books():
    field = entry.get()
    results_list.delete(0, tk.END)
    found = False
    for book in library:
        if field in book["title"] or field in book["author"]:
            results_list.insert(tk.END, f"{book['title']} WAS WRITTEN BY {book['author']}")
            found = True
    if not found:
        results_list.insert(tk.END, "No matches found.")

root = tk.Tk()
root.title("Mini Library Search")

tk.Label(root, text="ENTER BOOK TITLE OR AUTHOR NAME:",fg="darkred").pack(pady=5)
entry = tk.Entry(root, width=60)
entry.pack(pady=5)

tk.Button(root, text="Search",bg="black",fg="white",command=search_books).pack(pady=5)

results_list = tk.Listbox(root, width=60, height=10)
results_list.pack(pady=10)

root.mainloop()