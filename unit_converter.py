import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

entry = tkinter.Entry(width=10)
entry.insert(tkinter.END, string="0")
entry.grid(row=0, column=1)

label1 = tkinter.Label(text="Miles")
label1.grid(row=0, column=2)

label2 = tkinter.Label(text=" is equal to")
label2.grid(row=1, column=0)

label3 = tkinter.Label(text=" 0 ")
label3.grid(row=1, column=1)

label4 = tkinter.Label(text="Km")
label4.grid(row=1, column=2)

def miles_to_km():
    label3.config(text=f"{round(int(entry.get()) * 1.60934, 2)}")

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()