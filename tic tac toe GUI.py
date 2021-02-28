from tkinter import *
from tkinter import messagebox

root_game = Tk()
root_game.title("Tic Tac Toe")
root_game.configure(bg="black")
root_game.geometry("250x275")
game_still_going = True
winner           = None
player = 1
bx1 = "1"
bx2 = "2"
bx3 = "3"
bx4 = "4"
bx5 = "5"
bx6 = "6"
bx7 = "7"
bx8 = "8"
bx9 = "9"

def show(box):
    global bx1
    global bx2
    global bx3
    global bx4
    global bx5
    global bx6
    global bx7
    global bx8
    global bx9
    global player
    #----------------------for first box--------------------#
    if box == 1 and player == 1:
        b1.configure(text="X", fg="black")
        player = 2
        bx1 = "X"
    elif box == 1 and player == 2:
        b1.configure(text="O", fg="black")
        player = 1
        bx1 = "O"
    #----------------------for second box--------------------#

    elif box == 2 and player == 1:
        b2.configure(text="X", fg="black")
        player = 2
        bx2 = "X"
    elif box == 2 and player == 2:
        b2.configure(text="O", fg="black")
        player = 1
        bx2 = "O"

    #----------------------for third box--------------------#

    elif box == 3 and player == 1:
        b3.configure(text="X", fg="black")
        player = 2
        bx3 = "X"
    elif box == 3 and player == 2:
        b3.configure(text="O", fg="black")
        player = 1
        bx3 = "O"

    #----------------------for fourth box--------------------#

    elif box == 4 and player == 1:
        b4.configure(text="X", fg="black")
        player = 2
        bx4 = "X"
    elif box == 4 and player == 2:
        b4.configure(text="O", fg="black")
        player = 1
        bx4 = "O"
    
    #----------------------for fifth box--------------------#

    elif box == 5 and player == 1:
        b5.configure(text="X", fg="black")
        player = 2
        bx5 = "X"
    elif box == 5 and player == 2:
        b5.configure(text="O", fg="black")
        player = 1
        bx5 = "O"

    #----------------------for sixth box--------------------#

    elif box == 6 and player == 1:
        b6.configure(text="X", fg="black")
        player = 2
        bx6 = "X"
    elif box == 6 and player == 2:
        b6.configure(text="O", fg="black")
        player = 1
        bx6 = "O"

    #----------------------for seventh box--------------------#

    elif box == 7 and player == 1:
        b7.configure(text="X", fg="black")
        player = 2
        bx7 = "X"
    elif box == 7 and player == 2:
        b7.configure(text="O", fg="black")
        player = 1
        bx7 = "O"

    #----------------------for eighth box--------------------#

    elif box == 8 and player == 1:
        b8.configure(text="X", fg="black")
        player = 2
        bx8 = "X"
    elif box == 8 and player == 2:
        b8.configure(text="O", fg="black")
        player = 1
        bx8 = "O"

    #----------------------for nineth box--------------------#

    elif box == 9 and player == 1:
        b9.configure(text="X", fg="black")
        player = 2
        bx9 = "X"
    elif box == 9 and player == 2:
        b9.configure(text="O", fg="black")
        player = 1
        bx9 = "O"

#============================ for rows ================================#
    if bx1 == bx2 == bx3 == "X" or bx4 == bx5 == bx6 == "X" or bx7 == bx8 == bx9 =="X":
        player = "X"
        messagebox._show("Game End","player " + player + "Wins")

    if bx1 == bx2 == bx3 == "O" or bx4 == bx5 == bx6 == "O" or bx7 == bx8 == bx9 =="O":
        player = "O"
        messagebox._show("Game End","player " + player + "Wins")

#============================= for columns =============================#
    if bx1 == bx4 == bx7 == "X" or bx2 == bx5 == bx8 == "X" or bx3 == bx6 == bx9 =="X":
        player = "X"
        messagebox._show("Game End","player " + player + "Wins")

    if bx1 == bx4 == bx7 == "O" or bx2 == bx5 == bx8 == "O" or bx3 == bx6 == bx9 =="O":
        player = "O"
        messagebox._show("Game End","player " + player + "wins")

#============================= for diagonals ============================#
    if bx1 == bx5 == bx9 == "X" or bx3 == bx5 == bx7 =="X":
        player = "X"
        messagebox._show("Game End","player " + player + "Wins")

    if bx1 == bx5 == bx9 == "O" or bx3 == bx5 == bx7 =="O":
        player = "O"
        messagebox._show("Game End","player " + player + "wins")


       

f = Frame(bg="gray")

b1 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(1))
b1.place(x=2, y=3)

b2 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(2))
b2.place(x=85, y=3)

b3 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(3))
b3.place(x=168, y=3)

b4 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(4))
b4.place(x=2, y=93)

b5 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(5))
b5.place(x=85, y=93)

b6 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(6))
b6.place(x=168, y=93)

b7 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(7))
b7.place(x=2, y=183)

b8 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(8))
b8.place(x=85, y=183)

b9 = Button(root_game, text="", width=10, height=5,bg="lightgreen", command= lambda:show(9))
b9.place(x=168, y=183)
f.pack()


root_game.mainloop()