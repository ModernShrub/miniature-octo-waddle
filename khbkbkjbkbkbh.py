from tkinter import*
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Translator")
root.geometry("500x500")

label = Label(root, font=("Terminal", 20, "bold"), text = "Translator App")
label.place(relx=0.5, rely=0.1, anchor=CENTER)

label1 = Label(root, font=("Terminal", 20, "bold"), text = "Type text here: ")
label1.place(relx=0.5, rely=0.2, anchor=CENTER)

txt = Text(root, height=15, width=60, wrap=WORD, bd=0)
txt.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()