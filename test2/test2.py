# calculator app with graphical user interface  

from tkinter import *
from tkinter import messagebox
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def main():
    def click():
        a = int(e1.get())
        b = int(e2.get())
        choice = int(e3.get())
        if choice == 5:
            exit()
        else:
            if choice == 1:
                messagebox.showinfo("Result", add(a,b))
            elif choice == 2:
                messagebox.showinfo("Result", subtract(a,b))
            elif choice == 3:
                messagebox.showinfo("Result", multiply(a,b))
            elif choice == 4:
                messagebox.showinfo("Result", divide(a,b))
            else:
                messagebox.showinfo("Result", "Invalid choice")
    root = Tk()
    root.geometry("300x300")
    root.title("Calculator")
    l1 = Label(root, text="Enter first number")
    l1.pack()
    e1 = Entry(root)
    e1.pack()
    l2 = Label(root, text="Enter second number")
    l2.pack()
    e2 = Entry(root)
    e2.pack()
    l3 = Label(root, text="Enter your choice")
    l3.pack()
    e3 = Entry(root)
    e3.pack()
    b1 = Button(root, text="Calculate", command=click)
    b1.pack()
    root.mainloop()
main()





