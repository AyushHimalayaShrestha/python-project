import tkinter
import random

window = tkinter.Tk()

window.configure(bg='#333333')

window.title('My To Do List')

window.geometry('350x450')

tasks = []

# Creating functions

def update_selectionlist():
    # Clear the current list
    clear_selectionlist()

    # Update items in list
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_selectionlist():
    lb_tasks.delete(0, "end")

def add_task():
    # Get the task
    task = txt_input.get()
    # Append the task to list
    if task != '':
        tasks.append(task)
        update_selectionlist()
        display['text'] = ""
    else:
        display['text'] = "Please enter a task!"
    txt_input.delete(0, 'end')

def delete():
    task = lb_tasks.get('active')
    if task in tasks:
        tasks.remove(task)
    # Update list box
    update_selectionlist()
    display['text'] = "Task deleted!"

def delete_all():
    global tasks
    # Clear the list
    tasks = []
    update_selectionlist()
    display['text'] = "All tasks deleted!"

def choose_random():
    if tasks:
        task = random.choice(tasks)
        display['text'] = task
    else:
        display['text'] = "No tasks available!"

def number_of_task():
    number_of_tasks = len(tasks)
    msg = "Number of tasks: %s" % number_of_tasks
    display['text'] = msg

def exit():
    window.quit()

# Create Buttons and List options

title = tkinter.Label(window, text="To-Do-List", bg='lightyellow')
title.grid(row=0, column=0, columnspan=2, sticky='ew')

display = tkinter.Label(window, text="", bg='white')
display.grid(row=1, column=0, columnspan=2, sticky='ew')

txt_input = tkinter.Entry(window, width=15)
txt_input.grid(row=2, column=0, columnspan=2, sticky='ew')

btn_add_task = tkinter.Button(window, text="Add Task", fg='black', bg=None, command=add_task)
btn_add_task.grid(row=3, column=0, columnspan=2, sticky='ew')

btn_delete = tkinter.Button(window, text="Delete", fg='black', bg=None, command=delete)
btn_delete.grid(row=4, column=0, columnspan=2, sticky='ew')

btn_delete_all = tkinter.Button(window, text="Delete All", fg='black', bg=None, command=delete_all)
btn_delete_all.grid(row=5, column=0, columnspan=2, sticky='ew')

btn_choose_random = tkinter.Button(window, text="Choose Random", fg='black', bg=None, command=choose_random)
btn_choose_random.grid(row=6, column=0, columnspan=2, sticky='ew')

btn_number_of_task = tkinter.Button(window, text="Number of Tasks", fg='black', bg=None, command=number_of_task)
btn_number_of_task.grid(row=7, column=0, columnspan=2, sticky='ew')

btn_close = tkinter.Button(window, text="Exit", fg='white', bg="red", command=exit)
btn_close.grid(row=8, column=0, columnspan=2, sticky='ew')

lb_tasks = tkinter.Listbox(window)
lb_tasks.grid(row=3, column=2, rowspan=6, sticky='nsew')

# Configure grid to be responsive
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=3)
for i in range(9):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()
