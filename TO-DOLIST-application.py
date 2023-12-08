import tkinter as tk
from tkinter import messagebox

def add_task():
    task=entry.get()
    if task:
        task_listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning","Please enter a task.")

def remove_task():
    try:
        selected_task_index=task_listbox.curselection () [0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("warning","Please select a task to remove.")

def clear_task():
    task_listbox.delete(0,tk.END)


app=tk.Tk()
app.title("To-Do List Application")
app.geometry("600x600")
app.configure(bg="#F2F2F2")

title_label=tk.Label(app,text="Welcome to Vidhya's Tech-Nerds",font=("Arial",20),bg="#F2F2F2")
title_label.pack(pady=10)

title_label=tk.Label(app,text="To-Do List Application",font=("Arial",14),bg="#F2F2F2")
title_label.pack(pady=10)

entry=tk.Entry(app,width=40)
entry.pack(pady=10)

button_frame=tk.Frame(app,bg="#F2F2F2")
button_frame.pack()

add_button=tk.Button(button_frame,text="Add Task",command=add_task,bg="#63A69F",fg="white")
remove_button=tk.Button(button_frame,text="Remove Task",command=remove_task,bg="#E74C3C",fg="white")
clear_button=tk.Button(button_frame,text="Clear All",command=clear_task,bg="#3498DB",fg="white")

add_button.grid(row=0,column=0,padx=5)
remove_button.grid(row=0,column=1,padx=5)
clear_button.grid(row=0,column=2,padx=5)

task_listbox=tk.Listbox(app,width=50,bg="white")
task_listbox.pack(pady=10)

app.mainloop()                

entry=tk.Entry
