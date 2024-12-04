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
        self.cord = cord
        self.team = team
        if self.team == 1:
            self.name = colored(name, 'red')
        else:
            self.name = colored(name, 'blue')
    
    def go(self, cord1, cord2):
        self.cord = cord2
        figures[cord2] = figures[cord1]
        del figures[cord1]

    def __str__(self):
        return self.name

class Pawn(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)
        self.status = 1
    
    def check_move(self, cord1, cord2):
        x1, y1 = form_cord(cord1)
        x2, y2 = form_cord(cord2)
        if (self.status == 1) and (x1 == x2) and abs(y2 - y1) == 2 and not(cord2 in figures):
            self.status = 0
            return True
        elif x1 == x2 and abs(y1 - y2) == 1 and not(cord2 in figures):
            return True
        elif abs(y2 - y1) == 1 and abs(x2 - x1) == 1 and cord2 in figures:
            del figures[cord2]
            return True
        print(colored('Эта пешка не может совершить такой ход.', 'light_red'))
        return False

class Castle(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)
    
    def check_move(self, cord1, cord2):
        if cord2 in figures:
            if figures[cord2].team == figures[cord1].team:
                return self.castle_error()
            else:
                return self.is_row_clear(cord1, cord2)
        return self.is_row_clear(cord1, cord2)

    def is_row_clear(self, cord1, cord2):
        x1, y1 = form_cord(cord1)
        x2, y2 = form_cord(cord2)
        if x1 == x2:
            return self.check_vertical(x1, y1, y2)
        elif y1 == y2:
            return self.check_horizontal(y1, x1, x2)
        return self.castle_error()
        
    def check_vertical(self, x, y1, y2):
        for y in range(min(y1, y2) + 1, max(y1, y2)):
            cord = cord_to_letter(x + 1) + str(8 - y)
            if cord in figures:
                return self.castle_error()
        return True
        
    def check_horizontal(self, y, x1, x2):
        for x in range(min(x1, x2) + 1, max(x1, x2)):
            cord = cord_to_letter(x + 1) + str(y + 1)
            if cord in figures:
                return self.castle_error()
        return True
    
    def castle_error(self):
        print(colored('Эта ладья не может совершить такой ход.', 'light_red'))
        return False
        
class Horse(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)
        
    def possibilities(self):
        x = letter_to_cord(self.cord[0])
        y = int(self.cord[1])
        cords = [str(x + 2) + str(y + 1), str(x + 2) + str(y - 1), str(x - 2) + str(y + 1),
                 str(x - 2) + str(y - 1), str(x + 1) + str(y + 2), str(x + 1) + str(y - 2),
                 str(x - 1) + str(y + 2), str(x - 1) + str(y - 2)]
        possible_cords = [self.is_possible(cord) for cord in cords]
        return possible_cords

    def is_possible(self, cord):
        if cord[0] in '12345678' and cord[1] in '12345678':
            return cord_to_letter(int(cord[0])) + cord[1]
        return None
    
    def check_move(self, cord1, cord2):
        possible_cords = self.possibilities()
        if cord2 in possible_cords:
            if cord2 in figures:
                if figures[cord2].team != self.team:
                    return True
                self.horse_error()
                return False
            return True
        self.horse_error()
        return False
    
    def horse_error(self):
        print(colored('Этот конь не может совершить такой ход.', 'light_red'))
        return False

class Elephant(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)
    
class King(Figure):
    def __init__(self, name, cord, team):
        super().__init__(name, cord, team)

    def possibilities(self):
        x = letter_to_cord(self.cord[0])
        y = int(self.cord[1])
        cords = [str(x + 1) + str(y), str(x - 1) + str(y),
                 str(x) + str(y + 1), str(x) + str(y - 1),
                 str(x + 1) + str(y + 1), str(x + 1) + str(y - 1),
                 str(x - 1) + str(y - 1), str(x - 1) + str(y + 1)]
        possible_cords = [self.is_possible(cord) for cord in cords]
        return possible_cords

    def is_possible(self, cord):
        if cord[0] in '12345678' and cord[1] in '12345678':
            return cord_to_letter(int(cord[0])) + cord[1]
        return None
    
    def check_move(self, cord1, cord2):
        possible_cords = self.possibilities()
        if cord2 in possible_cords:
            if cord2 in figures:
                if figures[cord2].team != self.team:
                    return True
                self.king_error()
                return False
            return True
        self.king_error()
        return False
    
    def king_error(self):
        print(colored('Твой король не может совершить такой ход.', 'light_red'))
        return False

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


def check_pole(cord, turn):
    if cord in figures:
        if figures[cord].team == turn:
            return True
        else:
            print(colored('Хулиган! Это не твоя фигура.', 'light_red'))
            return False
    else:
        print(colored(f'На поле {cord} нет фигур.', 'light_red'))
        return False

def check_cord(cord):
    if len(cord) == 1:
        print(colored('Неверный формат ввода.', 'light_red'))
        return False
    elif cord[0] in 'abcdefgh' and cord[1] in '12345678':
        return True
    else:
        print(colored(f'Клетки "{cord}" не существует!', 'light_red'))
        return False

def change_turn(turn):
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    return turn

def global_check(user_input, turn):
    if user_input.count(' ') == 1:
        cord1, cord2 = user_input.split()
        if check_cord(cord1) and check_cord(cord2):
            if check_pole(cord1, turn) and figures[cord1].check_move(cord1, cord2):
                return True
    else:
        print(colored('Неверный формат ввода.', 'light_red'))
    return False

def get_input(turn):
    if turn == 1:
        color = 'red'
    else:
        color = 'blue'
    user_input = input(colored(colored('Ход ', 'light_cyan') + colored(f'Игрока {turn}:\n', str(color))))
    while not(global_check(user_input, turn)):
        user_input = input(colored(colored('Ход ', 'light_cyan') + colored(f'Игрока {turn}:\n', str(color))))
    return user_input.split()

def main():
    win = False
    turn = 1
    while not(win):
        board = form_board()
        draw_board(board)
        print()
        cord1, cord2 = get_input(turn)
        figures[cord1].go(cord1, cord2)
        turn = change_turn(turn)

main()