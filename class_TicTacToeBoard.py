# Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие методы:

class TicTacToeBoard():
    mark = ["X", "O"]
    counter = 0
    def __init__(self):
        self.field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.active = TicTacToeBoard.mark[0]
        self.win = True

    # new_game() – для создания новой игры;
    def new_game(self):
        return TicTacToeBoard()

    # get_field() – для получения поля (список списков);
    def get_field(self):
        return self.field

    # check_field() – для проверки, есть ли победитель;
    def check_field(self):
            TicTacToeBoard.counter += 1
            # Проверка по горизонтали
            if self.field[0][0] == self.field[0][1] == self.field[0][2] and self.field[0][0] != '-':
                return self.field[0][0]
            elif self.field[1][0] == self.field[1][1] == self.field[1][2] and self.field[1][0] != '-':
                return self.field[1][0]
            elif self.field[2][0] == self.field[2][1] == self.field[2][2] and self.field[2][0] != '-':
                return self.field[2][0]
            # Проверка по вертикали
            elif self.field[0][0] == self.field[1][0] == self.field[2][0] and self.field[0][0] != '-':
                return self.field[0][0]
            elif self.field[0][1] == self.field[1][1] == self.field[2][1] and self.field[0][1] != '-':
                return self.field[0][1]
            elif self.field[0][2] == self.field[1][2] == self.field[2][2] and self.field[0][2] != '-':
                return self.field[0][2]
            # Проверка по Диагонали
            elif self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != '-':
                return self.field[0][0]
            elif self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[0][2] != '-':
                return self.field[0][2]
            # Если ничья
            elif TicTacToeBoard.counter == 9:
                return "D"

    # make_move(row, col) – который устанавливает значение текущего хода в ячейку поля с координатами row, col
    def make_move(self, row, col):
        if self.win == True:
            if 0 <= row < 3 and 0 <= col < 3:
                if self.field[row][col] != '-':
                    print(f"Клетка {row + 1}:{col + 1} уже занята")
                    return 1
                else:
                    self.field[row][col] = self.active
                    self.active = TicTacToeBoard.mark[0] if self.active == TicTacToeBoard.mark[1] else \
                    TicTacToeBoard.mark[1]
                    result = self.check_field()
                    if result == None:
                        print("Продолжаем играть")
                        return 1
                    elif (result in 'XO'):
                        print(f"Победил игрок {result}")
                        self.win = False
                        return 0
                    elif result == "D":
                        print("Ничья")
                        self.win = False
                        return 0
                    return 1
            else:
                print('Повторите ход')
                return 1

board = TicTacToeBoard()
print(*board.get_field(), sep='\n')
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")