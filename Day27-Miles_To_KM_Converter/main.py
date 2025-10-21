### Mile to KM Converter ###

### importing the module
from tkinter import *

window=Tk()
window.title("Mile to KM Converter")
window.config(padx=100, pady=100)

### Entry - Input field for miles
mile_input=Entry(width=10)
mile_input.grid(column=1,row=0)
mile_input.insert(END, string="0")

###Label - Miles
miles_label=Label(text="Miles",font=("Times New Roman",12,"normal"))
miles_label.grid(column=2,row=0)


###Label - is equal to
equal_label=Label(text="is equal to",font=("Times New Roman",12,"normal"))
equal_label.grid(column=0,row=1)

### Label -KM Result
result_label=Label(text="0",font=("Times New Roman",12,"normal"))
result_label.grid(column=1,row=1)


###Label - KM
km_label=Label(text="KM",font=("Times New Roman",12,"normal"))
km_label.grid(column=2,row=1)


### Button - Calculate
def calculate_km():
    miles=float(mile_input.get())
    km=round(miles*1.60934,2)
    result_label.config(text=str(km))

button=Button(text="Calculate", command=calculate_km)
button.grid(column=1,row=2)


window.mainloop()