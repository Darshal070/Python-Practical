import tkinter as tk

def hello():
    print("Hello clicked")

root = tk.Tk()
root.title("Menu Example")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)

menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()
