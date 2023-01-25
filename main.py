import tkinter

window = tkinter.Tk()
window.title("My First GUI App")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    print("Click")
    my_label["text"] = input.get()

my_label=tkinter.Label(text="I am label.", font=("Arial", 24, "bold"))
#my_label.pack(side="top")
#my_label.place(x=0, y=100)
my_label.grid(row=0, column=0)
my_label.config(padx=30, pady=30)
#my_label["text"] = "New text"
#my_label.config(text="Another text", font=("Courier", 24, "italic"))


button = tkinter.Button(text="Click me.", command=button_clicked)
#button.pack()
button.grid(row=1, column=1)

input = tkinter.Entry(width=15)
input.grid(column=2, row=2)

button2 = tkinter.Button(text="New Button", command=button_clicked)
button2.grid(row=0, column=3)

window.mainloop()