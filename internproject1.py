import tkinter
import random

root = tkinter.Tk()
root.configure(bg = "white")
root.title("My To-Do-List")
root.geometry("200x500")

tasks = []
tasks = ["code", "eat", "sleep", "repeat"]


def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task"
    txt_input.delete(0, "end")

def del_all():
    global tasks
    tasks = []
    update_listbox()

def delete_task():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()

# def sort_dsc():
#     pass
    
def number_of_task():
    number_of_task = len(tasks)
    msg = ("Number of Task :", number_of_task)
    lbl_display["text"] = msg







lbl_title = tkinter.Label(root, text = "To-Do-List", bg = "white")
lbl_title.pack()

lbl_display = tkinter.Label(root, text = "", bg = "white")
lbl_display.pack()

txt_input = tkinter.Entry(root, width=15)
txt_input.pack()

btn_add_task = tkinter.Button(root, text = "Add task", fg = "green" , bg = "white", command = add_task)
btn_add_task.pack()

btn_del_all = tkinter.Button(root, text = "Delete All", fg = "green" , bg = "white", command = del_all)
btn_del_all.pack()

btn_delete_task = tkinter.Button(root, text = "Delete", fg = "green" , bg = "white", command = delete_task)
btn_delete_task.pack()

btn_sort_asc = tkinter.Button(root, text = "Sort ASC", fg = "green" , bg = "white", command = sort_asc)
btn_sort_asc.pack()

# btn_sort_dsc = tkinter.Button(root, text = "Sort DSC", fg = "green" , bg = "white", command = sort_dsc)
# btn_sort_dsc.pack()

btn_number_of_task = tkinter.Button(root, text = "Number of Task", fg = "green" , bg = "white", command = number_of_task)
btn_number_of_task.pack()

btn_exit = tkinter.Button(root, text = "Quit", fg = "green" , bg = "white", command = exit)
btn_exit.pack()

lb_tasks = tkinter.Listbox(root)
lb_tasks.pack()

root.mainloop()