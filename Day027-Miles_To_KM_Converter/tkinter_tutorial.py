from tkinter import *

window=Tk()

### changing the title of the window
window.title("My First GUI Application")

### changing the size of the window
window.minsize(width=500, height=300)

###Padding
window.config(padx=20, pady=20)

###Label
label=Label(text="Hello",font=("Times New Roman",24,"bold"))
#label.pack()
label.grid(column=0, row=0)

label["text"]="New Text"
label.config(text="Another New Text")
label.config(padx=50, pady=50)
###Buttons

def action():
    print("Button Clicked!")

def change_txt():
    text=entry.get()
    label.config(text=text)
button =Button(text="Click Me", command=change_txt)
#button.pack()
#button.place(x=200,y=100)
button.grid(column=1, row=1)

###Entry
entry=Entry(width=30)
#entry.pack()
entry.grid(column=2, row=2)


###Text
text=Text(height=5, width=30)
##Putting cursor in textbox
text.focus()
#text.pack()


###Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox=Spinbox(from_=0, to_=10, width=5, command=spinbox_used)
#spinbox.pack()


###Scale
def scale_used(value):
    print(value)
scale=Scale(from_=0, to=100, command=scale_used)
#scale.pack()


###CheckBox
def checkbutton_used():
    print(checked_state.get())
checked_state=IntVar()
checkbutton=Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
#checkbutton.pack()


###Radiobutton
def radio_used():
    print(radio_state.get())
radio_state=IntVar()
radiobutton1=Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2=Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
#radiobutton1.pack()
#radiobutton2.pack()


###Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox=Listbox(height=4)
fruits=["Apple","Banana","Cherry","Date"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
#listbox.pack()

window.mainloop()