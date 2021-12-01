from tkinter import*
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Translator")
root.geometry("1200x500")

label = Label(root, font=("Terminal", 20, "bold"), text = "Translator App")
label.place(relx=0.5, rely=0.1, anchor=CENTER)

label1 = Label(root, font=("Terminal", 10, "bold"), text = "Type text here: ")
label1.place(relx=0.1, rely=0.3, anchor=CENTER)

stxt = Text(root, height=15, width=60, wrap=WORD, bd=0)
stxt.place(relx=0.21,rely=0.6,anchor=CENTER)

langlist = LANGUAGES.values()
langlist = list(langlist)
print(langlist)
sdrp = ttk.Combobox(root, state="readonly", width=30,values=langlist)
sdrp.place(relx=0.25,rely=0.3,anchor=CENTER)
sdrp.set("english")

label2 = Label(root, font=("Terminal", 10, "bold"), text = "Translated text: ")
label2.place(relx=0.69, rely=0.3, anchor=CENTER)

otxt = Text(root, height=15, width=60, wrap=WORD, bd=0)
otxt.place(relx=0.79,rely=0.6,anchor=CENTER)

odrp = ttk.Combobox(root, state="readonly", width=30,values=langlist)
odrp.place(relx=0.85,rely=0.3,anchor=CENTER)
odrp.set("select output language")

btn = Button(root, text="Translate", bg="navajo white", relief=FLAT, font=("Terminal", 10, "bold"))
btn.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()