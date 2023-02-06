import tkinter as tk

board = [[" " for x in range(3)] for y in range(3)]


def print_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = board[i][j]
            if board[i][j] == "X":
                buttons[i][j]["bg"] = "red"
            elif board[i][j] == "O":
                buttons[i][j]["bg"] = "green"
            else:
                buttons[i][j]["bg"] = "white"


def make_move(player, i, j):
    if board[i][j] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    board[i][j] = player
    return True


def check_win(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True
    return False


def button_click(i, j):
    global player
    if make_move(player, i, j):
        print_board()
        if check_win(player):
            print(f"{player} wins")
            root.quit()
        player = "X" if player == "O" else "O"


root = tk.Tk()
root.configure(bg='white')
buttons = [[tk.Button(root, command=lambda i=i, j=j: button_click(i, j), width=10, height=5, bg='white') for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

player = "X"
print_board()
root.mainloop()
