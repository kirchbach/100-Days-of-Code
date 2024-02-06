from tkinter import *
window = Tk()
window.title("Miles to Km")
window.config(padx=20, pady=20)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

km = Label(text="Km")
km.grid(row=1, column=2)

result = Label(text="0")
result.grid(row=1, column=1)

def miles_to_km():
    result.config(text=int(entry.get())*1.60934)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)

entry = Entry(text="0", width=4)
entry.grid(row=0, column=1)




window.mainloop()