import tkinter as tk
from tkinter import messagebox

# Global variable to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name.strip() == '' or phone.strip() == '':
        messagebox.showerror("Error", "Name and Phone number are required!")
        return

    contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
    messagebox.showinfo("Success", "Contact added successfully!")

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if search_term in contact['Name'].lower() or search_term in contact['Phone']:
            contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to delete a contact
def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        del contacts[index]
        view_contacts()

# Create the main Tkinter window
root = tk.Tk()
root.title("Contact Management System")

# Create input fields and labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Add buttons for adding, viewing, searching, and deleting contacts
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

search_label = tk.Label(root, text="Search:")
search_label.grid(row=6, column=0, padx=5, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1, padx=5, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=6, column=2, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Create a listbox to display contacts
contact_list = tk.Listbox(root)
contact_list.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

root.mainloop()