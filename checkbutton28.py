import tkinter as tk

def show():
    print("C:", var1.get(), "Java:", var2.get())

root = tk.Tk()
root.title("Checkbutton Example")

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(root, text="C", variable=var1)
c2 = tk.Checkbutton(root, text="Java", variable=var2)

c1.pack()
c2.pack()

btn = tk.Button(root, text="Submit", command=show)
btn.pack()

root.mainloop()
