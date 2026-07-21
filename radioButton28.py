import tkinter as tk

def show():
    print("Selected:", var.get())

root = tk.Tk()
root.title("Radiobutton Example")

var = tk.StringVar()

r1 = tk.Radiobutton(root, text="Male", variable=var, value="Male")
r2 = tk.Radiobutton(root, text="Female", variable=var, value="Female")

r1.pack()
r2.pack()

btn = tk.Button(root, text="Submit", command=show)
btn.pack()

root.mainloop()
