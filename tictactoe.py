from tkinter import *

# Main window
root = Tk()
root.title("Tic Tac Toe")
root.geometry("350x400")
root.resizable(False, False)

# Title
title = Label(root, text="Tic Tac Toe",
              font=("Arial", 24, "bold"))
title.pack(pady=20)

# Frame for buttons
frame = Frame(root)
frame.pack()

# Create 3x3 grid buttons
for row in range(3):
    for col in range(3):

        btn = Button(frame,
                     text="",
                     font=("Arial", 24, "bold"),
                     width=5,
                     height=2)

        btn.grid(row=row, column=col, padx=5, pady=5)

# Restart button
restart = Button(root,
                 text="Restart",
                 font=("Arial", 14),
                 width=10)

restart.pack(pady=20)

# Run window
root.mainloop()