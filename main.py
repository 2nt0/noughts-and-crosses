from tkinter import *

def check_win(array):
    combinations = [[0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]
    for sub in combinations:
        if array[sub[0]] == array[sub[1]] == array[sub[2]] and array[sub[0]] != '-':
            return array[sub[0]]
            break

array = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
move = 'X'

root = Tk()
root.geometry("300x300")
root.title('BRNaC (v0.1)')

for x in range(3):
    Grid.columnconfigure(root, x, weight=1)
    Grid.rowconfigure(root, x, weight=1)
    for y in range(3):
        btn = Button(root)
        btn.grid(column=x, row=y, sticky=N+S+E+W)

root.mainloop()
'''
while True:
    print('\n', array[0], array[1], array[2], '\n', array[3], array[4], array[5], '\n', array[6], array[7], array[8])
    win = check_win(array)
    if win:
        print(win, 'win')
        break
    elif move == 'O':
        move = 'X'
    else:
        move = 'O'
    print(move, 'move')
    square = int(input('Make your move '))
    while array[square] != '-':
        square = int(input('Invalid move! Make your move '))
    array[square] = move'''