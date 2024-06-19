import tkinter 
from tkinter import ttk


window=tkinter.Tk()
window.title("Signup Form")
window.geometry("340x440")
#window.config(bg="#333333")

#Creating widget
signup_label=tkinter.Label(window, text="SignUp")
name_label=tkinter.Label(window,text="Name : ")
name_entry=tkinter.Entry(window)
address_label=tkinter.Label(window,text="Address : ")
address_entry=tkinter.Entry(window)
contact_label=tkinter.Label(window, text="Contact No. : ")
contact_entry=tkinter.Entry(window)

choice=["15-20","20-25","25-30","30-35","35-40","40-45","45-50","50-55","55-60","60-65"]
age_label=tkinter.Label(window, text="Age : ")
age_dropdown=ttk.Combobox(window,value=choice)


#Placing widgets
signup_label.grid(row=0, column=0,columnspan=2)
name_label.grid(row=1,column=0)
name_entry.grid(row=1, column=1)
address_label.grid(row=2,column=0)
address_entry.grid(row=2,column=1)
contact_label.grid(row=3,column=0)
contact_entry.grid(row=3,column=1)
age_label.grid(row=4,column=0)
age_dropdown.grid(row=4,column=1)

window.mainloop()