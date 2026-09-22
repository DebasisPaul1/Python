from tkinter import *

root = Tk()
root.title("Tic Tac Toe")
root.geometry("350x430")

player = "X"
buttons = []


def click(button):
    global player

    if button["text"] == "":
        button["text"] = player

        if winner():
            result.config(text=player + " Wins!")
            disable_buttons()
        elif all(button["text"] != "" for button in buttons):
            result.config(text="Draw!")
        else:
            if player == "X":
                player = "O"
            else:
                player = "X"

            result.config(text="Player " + player + "'s Turn")


def winner():
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for a, b, c in wins:
        if (buttons[a]["text"] != "" and
            buttons[a]["text"] == buttons[b]["text"] and
            buttons[b]["text"] == buttons[c]["text"]):
            return True

    return False


def disable_buttons():
    for button in buttons:
        button.config(state=DISABLED)


def restart():
    global player

    player = "X"

    for button in buttons:
        button.config(text="", state=NORMAL)

    result.config(text="Player X's Turn")


title = Label(
    root,
    text="Tic Tac Toe",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)


result = Label(
    root,
    text="Player X's Turn",
    font=("Arial", 14, "bold")
)
result.pack(pady=5)


frame = Frame(root)
frame.pack()


for i in range(9):
    button = Button(
        frame,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2
    )

    button.config(command=lambda b=button: click(b))

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    buttons.append(button)


restart_button = Button(
    root,
    text="Restart",
    font=("Arial", 14),
    command=restart
)

restart_button.pack(pady=20)


root.mainloop()


restart.pack(pady=20)

# Run window
root.mainloop()
