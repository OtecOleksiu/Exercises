import random
import time


class Player:
    def __init__(self, number):
        self.number = number
        self.inpt_lst = []

    def __str__(self):
        return f'player{self.number}\'s list[{self.inpt_lst}]'


class Board:
    def __init__(self):
        self.row1 = f'{"-------------"}\n{"|   |   |   |"}'
        self.row2 = f'{"-------------"}\n{"|   |   |   |"}\n{"-------------"}'
        self.row3 = f'{"|   |   |   |"}\n{"-------------"}'

    def __str__(self):
        return f'{self.row1}\n{self.row2}\n{self.row3}'

    def board_fill(self, x, y, z):
        if z == 'a':
            self.row1 = self.row1.split('|')
            self.row1[x] = f' {y} '
            self.row1 = '|'.join(self.row1)
        elif z == 'b':
            self.row2 = self.row2.split('|')
            self.row2[x - 3] = f' {y} '
            self.row2 = '|'.join(self.row2)
        elif z == 'c':
            self.row3 = self.row3.split('|')
            self.row3[x - 11] = f' {y} '
            self.row3 = '|'.join(self.row3)


class Game:
    def __init__(self, player, cpu, board):
        self.player = player
        self.cpu = cpu
        self.board = board
        self.existing_numbers = []

    def inpt(self):
        try:
            nmbr = int(input('pick an empty space (1-9): '))
            while nmbr > 9 or nmbr == 0 or nmbr in self.existing_numbers:
                print('I said 1-9 that is empty')
                nmbr = int(input('pick an empty space (1-9): '))

        except Exception as _ex:
            print('I said 1-9 that is empty')
            nmbr = int(input('pick an empty space (1-9): '))
            while nmbr > 9 or nmbr == 0 or nmbr in self.existing_numbers:
                print('I said 1-9 that is empty')
                nmbr = int(input('pick an empty space (1-9): '))
        self.existing_numbers.append(nmbr)
        self.player.inpt_lst.append(nmbr)
        if nmbr in range(1, 4):
            flag = 'a'
            return flag, nmbr
        elif nmbr in range(4, 7):
            flag = 'b'
            return flag, nmbr
        elif nmbr in range(7, 10):
            flag = 'c'
            return flag, nmbr

    def logic_emergency(self):
        if 1 in self.player.inpt_lst and 2 in self.player.inpt_lst and 3 not in self.cpu.inpt_lst:
            return 3
        elif 2 in self.player.inpt_lst and 3 in self.player.inpt_lst and 1 not in self.cpu.inpt_lst:
            return 1
        elif 4 in self.player.inpt_lst and 5 in self.player.inpt_lst and 6 not in self.cpu.inpt_lst:
            return 6
        elif 5 in self.player.inpt_lst and 6 in self.player.inpt_lst and 4 not in self.cpu.inpt_lst:
            return 4
        elif 7 in self.player.inpt_lst and 8 in self.player.inpt_lst and 9 not in self.cpu.inpt_lst:
            return 9
        elif 8 in self.player.inpt_lst and 9 in self.player.inpt_lst and 7 not in self.cpu.inpt_lst:
            return 7
        elif 1 in self.player.inpt_lst and 4 in self.player.inpt_lst and 7 not in self.cpu.inpt_lst:
            return 7
        elif 4 in self.player.inpt_lst and 7 in self.player.inpt_lst and 1 not in self.cpu.inpt_lst:
            return 1
        elif 2 in self.player.inpt_lst and 5 in self.player.inpt_lst and 8 not in self.cpu.inpt_lst:
            return 8
        elif 5 in self.player.inpt_lst and 8 in self.player.inpt_lst and 2 not in self.cpu.inpt_lst:
            return 2
        elif 3 in self.player.inpt_lst and 6 in self.player.inpt_lst and 9 not in self.cpu.inpt_lst:
            return 9
        elif 6 in self.player.inpt_lst and 9 in self.player.inpt_lst and 3 not in self.cpu.inpt_lst:
            return 3
        elif 1 in self.player.inpt_lst and 5 in self.player.inpt_lst and 9 not in self.cpu.inpt_lst:
            return 9
        elif 9 in self.player.inpt_lst and 5 in self.player.inpt_lst and 1 not in self.cpu.inpt_lst:
            return 1
        elif 3 in self.player.inpt_lst and 5 in self.player.inpt_lst and 7 not in self.cpu.inpt_lst:
            return 7
        elif 7 in self.player.inpt_lst and 5 in self.player.inpt_lst and 3 not in self.cpu.inpt_lst:
            return 3
        elif 1 in self.player.inpt_lst and 3 in self.player.inpt_lst and 2 not in self.cpu.inpt_lst:
            return 2
        elif 4 in self.player.inpt_lst and 6 in self.player.inpt_lst and 5 not in self.cpu.inpt_lst:
            return 5
        elif 7 in self.player.inpt_lst and 9 in self.player.inpt_lst and 8 not in self.cpu.inpt_lst:
            return 8
        elif 1 in self.player.inpt_lst and 7 in self.player.inpt_lst and 4 not in self.cpu.inpt_lst:
            return 4
        elif 2 in self.player.inpt_lst and 8 in self.player.inpt_lst and 5 not in self.cpu.inpt_lst:
            return 5
        elif 3 in self.player.inpt_lst and 9 in self.player.inpt_lst and 6 not in self.cpu.inpt_lst:
            return 6
        elif 1 in self.player.inpt_lst and 9 in self.player.inpt_lst and 5 not in self.cpu.inpt_lst:
            return 5
        elif 3 in self.player.inpt_lst and 7 in self.player.inpt_lst and 5 not in self.cpu.inpt_lst:
            return 5

    def logic_cpu_win(self):
        if 1 in self.cpu.inpt_lst and 2 in self.cpu.inpt_lst and 3 not in self.player.inpt_lst:
            return 3
        elif 2 in self.cpu.inpt_lst and 3 in self.cpu.inpt_lst and 1 not in self.player.inpt_lst:
            return 1
        elif 4 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst and 6 not in self.player.inpt_lst:
            return 6
        elif 5 in self.cpu.inpt_lst and 6 in self.cpu.inpt_lst and 4 not in self.player.inpt_lst:
            return 4
        elif 7 in self.cpu.inpt_lst and 8 in self.cpu.inpt_lst and 9 not in self.player.inpt_lst:
            return 9
        elif 8 in self.cpu.inpt_lst and 9 in self.cpu.inpt_lst and 7 not in self.player.inpt_lst:
            return 7
        elif 1 in self.cpu.inpt_lst and 4 in self.cpu.inpt_lst and 7 not in self.player.inpt_lst:
            return 7
        elif 4 in self.cpu.inpt_lst and 7 in self.cpu.inpt_lst and 1 not in self.player.inpt_lst:
            return 1
        elif 2 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst and 8 not in self.player.inpt_lst:
            return 8
        elif 5 in self.cpu.inpt_lst and 8 in self.cpu.inpt_lst and 2 not in self.player.inpt_lst:
            return 2
        elif 3 in self.cpu.inpt_lst and 6 in self.cpu.inpt_lst and 9 not in self.player.inpt_lst:
            return 9
        elif 6 in self.cpu.inpt_lst and 9 in self.cpu.inpt_lst and 3 not in self.player.inpt_lst:
            return 3
        elif 1 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst and 9 not in self.player.inpt_lst:
            return 9
        elif 9 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst and 1 not in self.player.inpt_lst:
            return 1
        elif 3 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst and 7 not in self.player.inpt_lst:
            return 7
        elif 7 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst and 3 not in self.player.inpt_lst:
            return 3
        elif 1 in self.cpu.inpt_lst and 3 in self.cpu.inpt_lst and 2 not in self.player.inpt_lst:
            return 2
        elif 4 in self.cpu.inpt_lst and 6 in self.cpu.inpt_lst and 5 not in self.player.inpt_lst:
            return 5
        elif 7 in self.cpu.inpt_lst and 9 in self.cpu.inpt_lst and 8 not in self.player.inpt_lst:
            return 8
        elif 1 in self.cpu.inpt_lst and 7 in self.cpu.inpt_lst and 4 not in self.player.inpt_lst:
            return 4
        elif 2 in self.cpu.inpt_lst and 8 in self.cpu.inpt_lst and 5 not in self.player.inpt_lst:
            return 5
        elif 3 in self.cpu.inpt_lst and 9 in self.cpu.inpt_lst and 6 not in self.player.inpt_lst:
            return 6
        elif 1 in self.cpu.inpt_lst and 9 in self.cpu.inpt_lst and 5 not in self.player.inpt_lst:
            return 5
        elif 3 in self.cpu.inpt_lst and 7 in self.cpu.inpt_lst and 5 not in self.player.inpt_lst:
            return 5

    def cpu_inpt(self):
        lgc0 = self.logic_cpu_win()
        lgc = self.logic_emergency()
        if type(lgc0) == int:
            nmbr2 = lgc0
            # print(f'le win{type(lgc0)}, {nmbr2}')
        elif type(lgc) == int and type(lgc0) != int:
            nmbr2 = lgc
            # print(f'le true{type(lgc)}, {nmbr2}')
        elif type(lgc0) != int and type(lgc) != int and 5 not in self.existing_numbers:
            nmbr2 = 5
        elif len(self.existing_numbers) == 1 and self.existing_numbers[0] == 5:
            rnge = [1, 3, 7, 9]
            nmbr2 = random.choice(rnge)
        elif 1 in self.player.inpt_lst and 9 in self.player.inpt_lst or 3 in self.player.inpt_lst and 7 in self.player.inpt_lst:
            rnge = [2, 4, 6, 8]
            nmbr2 = random.choice(rnge)
        else:
            rnge = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            nmbr2 = random.choice(rnge)
            # print(f'le false{type(lgc)}, {nmbr2}')
            # print(f'{nmbr2=}')
            # print(nmbr2 in self.existing_numbers)
            # print(rnge)
            while nmbr2 in self.existing_numbers:
                rnge.pop(rnge.index(nmbr2))
                nmbr2 = random.choice(rnge)
            #     print(f'nmbr2 in while = {nmbr2}')
            # print(f'final numbr2: {nmbr2}')
            # print(rnge)

        self.existing_numbers.append(nmbr2)
        self.cpu.inpt_lst.append(nmbr2)
        if nmbr2 in range(1, 4):
            flag = 'a'
            return flag, nmbr2
        elif nmbr2 in range(4, 7):
            flag = 'b'
            return flag, nmbr2
        elif nmbr2 in range(7, 10):
            flag = 'c'
            return flag, nmbr2

    def win_condition(self):
        if 1 in self.player.inpt_lst and 2 in self.player.inpt_lst and 3 in self.player.inpt_lst or 4 in self.player.inpt_lst \
                and 5 in self.player.inpt_lst and 6 in self.player.inpt_lst or 7 in self.player.inpt_lst and 8 in self.player.inpt_lst \
                and 9 in self.player.inpt_lst or 1 in self.player.inpt_lst and 4 in self.player.inpt_lst and 7 in self.player.inpt_lst \
                or 2 in self.player.inpt_lst and 5 in self.player.inpt_lst and 8 in self.player.inpt_lst or 3 in self.player.inpt_lst \
                and 6 in self.player.inpt_lst and 9 in self.player.inpt_lst or 1 in self.player.inpt_lst and 5 in self.player.inpt_lst \
                and 9 in self.player.inpt_lst or 3 in self.player.inpt_lst and 5 in self.player.inpt_lst and 7 in self.player.inpt_lst:
            print('player won')
            return True
        elif 1 in self.cpu.inpt_lst and 2 in self.cpu.inpt_lst and 3 in self.cpu.inpt_lst or 4 in self.cpu.inpt_lst \
                and 5 in self.cpu.inpt_lst and 6 in self.cpu.inpt_lst or 7 in self.cpu.inpt_lst and 8 in self.cpu.inpt_lst \
                and 9 in self.cpu.inpt_lst or 1 in self.cpu.inpt_lst and 4 in self.cpu.inpt_lst and 7 in self.cpu.inpt_lst \
                or 2 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst and 8 in self.cpu.inpt_lst or 3 in self.cpu.inpt_lst \
                and 6 in self.cpu.inpt_lst and 9 in self.cpu.inpt_lst or 1 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst \
                and 9 in self.cpu.inpt_lst or 3 in self.cpu.inpt_lst and 5 in self.cpu.inpt_lst and 7 in self.cpu.inpt_lst:
            print('cpu won')
            return True

    def tst(self):
        while True:
            x = self.inpt()
            print(self.player.inpt_lst)
            self.board.board_fill(x[1], 'x', x[0])
            print(self.board)
            print(self.existing_numbers)
            if self.win_condition():
                j = input('play again? y/n ')
                if j == 'y':
                    main()
                    break
                else:
                    break
            if len(self.existing_numbers) == 9:
                print('tie')
                j = input('play again? y/n ')
                if j == 'y':
                    main()
                    break
                else:
                    break

            print('im thinking')
            time.sleep(2)
            y = self.cpu_inpt()
            self.board.board_fill(y[1], 'o', y[0])
            print(self.board)
            print(self.existing_numbers)
            print('-' * 25)
            if self.win_condition():
                j = input('play again? y/n ')
                if j == 'y':
                    main()
                    break
                else:
                    break


def main():
    player1 = Player(1)
    cpu = Player(2)
    board1 = Board()
    game = Game(player1, cpu, board1)
    game.tst()


if __name__ == '__main__':
    main()
