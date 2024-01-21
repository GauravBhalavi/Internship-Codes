import tkinter as tk
from tkinter import ttk

# Data Storage
contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    update_contact_list()

    # Clear entry fields for next entry
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

def search_contact():
    search_term = search_entry.get()
    search_result = [contact for contact in contacts if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]]
    contact_list.delete(0, tk.END)
    for contact in search_result:
        contact_list.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        contacts.pop(selected_index[0])
        update_contact_list()

app = tk.Tk()
app.title("Contact Book")

# Input Fields
name_label = ttk.Label(app, text="Name:")
name_label.grid(row=0, column=0)
name_entry = ttk.Entry(app)
name_entry.grid(row=0, column=1)

phone_label = ttk.Label(app, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = ttk.Entry(app)
phone_entry.grid(row=1, column=1)

email_label = ttk.Label(app, text="Email:")
email_label.grid(row=2, column=0)
email_entry = ttk.Entry(app)
email_entry.grid(row=2, column=1)

address_label = ttk.Label(app, text="Address:")
address_label.grid(row=3, column=0)
address_entry = ttk.Entry(app)
address_entry.grid(row=3, column=1)

# Buttons
add_button = ttk.Button(app, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2)

search_label = ttk.Label(app, text="Search:")
search_label.grid(row=5, column=0)
search_entry = ttk.Entry(app)
search_entry.grid(row=5, column=1)

search_button = ttk.Button(app, text="Search", command=search_contact)
search_button.grid(row=6, column=0, columnspan=2)

delete_button = ttk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.grid(row=7, column=0, columnspan=2)

# Listbox to Display Contacts
contact_list = tk.Listbox(app)
contact_list.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

update_contact_list()

app.mainloop()
