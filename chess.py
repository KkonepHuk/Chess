'''
---------------------------------
| л | к | с | k | ф | с | к | л | 8
---------------------------------
| п | п | п | п | п | п | п | п | 7
---------------------------------
|   |   |   |   |   |   |   |   | 6
---------------------------------
|   |   |   |   |   |   |   |   | 5
---------------------------------
|   |   |   |   |   |   |   |   | 4
---------------------------------
|   |   |   |   |   |   |   |   | 3
---------------------------------
| п | п | п | п | п | п | п | п | 2
---------------------------------
| л | к | с | ф | k | с | к | л | 1
---------------------------------
  a   b   c   d   e   f   g   h
'''
from termcolor import colored

class Figure:
    def __init__(self, name, cord, team):
        self.x, self.y = form_cord(cord)
        self.team = team
        if self.team == 1:
            self.name = colored(name, 'red')
        else:
            self.name = colored(name, 'blue')
    
    def go(self, cord1, cord2):
        self.x, self.y = form_cord(cord2)
        figures[cord2] = figures[cord1]
        del figures[cord1]

    def __str__(self):
        return self.name

class Pawn(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)

class Castle(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)

class Horse(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)

class Elephant(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)
    
class King(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)

class Queen(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)



def letter_to_cord(letter):
    data = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6,'g' : 7, 'h' : 8}
    return data[letter]

def cord_to_letter(cord):
    data = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h'}
    return data[cord]

def form_cord(cord):
        x = letter_to_cord(cord[0]) - 1
        y = 8 - int(cord[1])
        return (x, y)

#Создание доски с фигурами
def form_board():
    board = [[' ' for i in range(8)] for j in range(8)]
    for cord in figures:
        x, y = form_cord(cord)
        board[y][x] = str(figures[cord]) 
    return board

#Отрисовка доски
def draw_board(board):
    num = 8
    for row in board:
        print('-' * 32)
        print('| ' + ' | '.join([str(elem) for elem in row]) + ' |  ' + str(num))
        num -= 1
    print()
    print('  a   b   c   d   e   f   g   h   ')

#Фигуры на доске
figures = {'a1': Castle('л', 'a1', 1), 'h1': Castle('л', 'h1', 1), 'b1': Horse('к', 'b1', 1), 'g1': Horse('к', 'g1', 1), 'g8': Horse('к', 'g8', 2),
           'c1': Elephant('с', 'c1', 1), 'f1': Elephant('с', 'f1', 1), 'e1': King('k', 'e1', 1), 'd1': Queen('ф', 'd1', 1), 
           'a8': Castle('л', 'a8', 2), 'h8': Castle('л', 'h8', 2), 'b8': Horse('к', 'b8', 2), 'g8': Horse('к', 'g8', 2), 
           'c8': Elephant('с', 'c8', 2), 'f8': Elephant('с', 'f8', 2), 'd8': King('k', 'd8', 2), 'e8': Queen('ф', 'e8', 2)}
for i in range(8):
    figures[cord_to_letter(i + 1) + '7'] = Pawn('п', cord_to_letter(i + 1) + '7', 2)
    figures[cord_to_letter(i + 1) + '2'] = Pawn('п', cord_to_letter(i + 1) + '2', 1)

def move(cord1, cord2, turn):
    if cord1 in figures:
        if figures[cord1].team == turn:
            figures[cord1].go(cord1, cord2)
    else:
        print('Что - то не так')

def change_turn(turn):
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    return turn

def main():
    win = False
    turn = 1
    while not(win):
        board = form_board()
        draw_board(board)
        print()
        cord1, cord2 = input(f'Ход Игрока {turn}:\n').split()
        move(cord1, cord2, turn)
        turn = change_turn(turn)

main()