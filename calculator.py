from tkinter import *
root=Tk()
root.title("Basic Calculator")
root.geometry("400x400")
root.resizable(False, False)
root["bg"]='#36454F'

# Entry box
text1 = Entry(root, width=20, font=("Arial", 24), borderwidth=5, justify="right")
text1.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Functions
def click(value):
    current = text1.get()

    if value == "x":
        text1.insert(END, "*")
    elif value == "^":
        text1.insert(END, "**")
    else:
        text1.insert(END, value)

def clear():
    text1.delete(0, END)

def backspace():
    current = text1.get()
    text1.delete(0, END)
    text1.insert(0, current[:-1])

def calculate():
    try:
        result = eval(text1.get())
        text1.delete(0, END)
        text1.insert(0, result)
    except:
        text1.delete(0, END)
        text1.insert(0, "Error")

# Button list
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("%",1,4),
    ("4",2,0), ("5",2,1), ("6",2,2), ("x",2,3), ("^",2,4),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("+",3,4),
    ("0",4,0), (".",4,1), ("C",4,2), ("AC",4,3), ("=",4,4)
]

# Create buttons
for (text, row, col) in buttons:

    if text == "=":
        Button(root, text=text, width=5, height=2,bg='lavender',
               command=calculate).grid(row=row, column=col, padx=2, pady=2)

    elif text == "AC":
        Button(root, text=text, width=5, height=2, bg='grey',
               command=clear).grid(row=row, column=col, padx=2, pady=2)

    elif text == "C":
        Button(root, text=text, width=5, height=2,bg='#86CEFA',
               command=backspace).grid(row=row, column=col, padx=2, pady=2)

    else:
        Button(root, text=text, width=5, height=2,bg='#FAF3E0',
               command=lambda t=text: click(t)).grid(row=row, column=col, padx=2, pady=2)
               
root.mainloop()