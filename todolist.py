import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        
        # Configure root grid
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create frame
        self.frame = tk.Frame(root)
        self.frame.grid(row=1, column=0, pady=10, padx=10, sticky='nsew')
        
        # Configure frame grid
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        # Create listbox
        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=10,
            bd=0,
            selectbackground="#a6a6a6"
        )
        self.listbox.grid(row=0, column=0, sticky='nsew')
        
        
        # Create entry box
        self.entry = tk.Entry(
            root,
            font=('arial', 15)
        )
        self.entry.grid(row=0, column=0, pady=10, padx=10, sticky='ew')
        
        # Create button frame
        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=2, column=0, pady=10, padx=10, sticky='ew')
        
        # Configure button frame grid
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)

        
        # Add buttons with padding
        self.add_button = tk.Button(
            self.button_frame,
            text='Add',
            command=self.add_task,
            bg="green",
            fg="white"
        )
        self.add_button.grid(row=0, column=0, padx=5, sticky='ew')
        
        self.delete_button = tk.Button(
            self.button_frame,
            text='Delete',
            command=self.delete_task
        )
        self.delete_button.grid(row=0, column=1, padx=5, sticky='ew')
        
        self.reset_button = tk.Button(
            self.button_frame,
            text='Reset',
            command=self.clear_all
        )
        self.reset_button.grid(row=0, column=2, padx=5, sticky='ew')

        self.quit_button=tk.Button(
            self.button_frame,
            text="Exit",
            command=self.quit,
            bg="red",
            fg="white"
        )
        self.quit_button.grid(row=0,column=3,padx=5,sticky='ew')
        
        # Configure widget expansion and filling
        self.configure_responsive_layout()

    def configure_responsive_layout(self):
        # Configure listbox and scrollbar to expand and fill
        self.listbox.grid(row=0, column=0, sticky='nsew')
        
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Configure entry box to expand horizontally
        self.entry.grid(row=0, column=0, pady=10, padx=10, sticky='ew')

        # Configure button frame to expand horizontally
        self.button_frame.grid(row=2, column=0, pady=10, padx=10, sticky='ew')
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def clear_all(self):
        self.listbox.delete(0, tk.END)

    def quit(self):
        self.listbox.quit()    


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
