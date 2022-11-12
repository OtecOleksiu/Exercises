import random

value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit = {'S': '♠', 'C': '♣', 'D': '♦', 'H': '♥'}
suit1 = ('S', 'C', 'D', 'H')


class Card:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}{suit[self.y]}'

    def __gt__(self, other):
        if value.index(self.x) == value.index(other.x):
            return suit1.index(self.y) > suit1.index(other.y)
        return value.index(self.x) > value.index(other.x)

    def __lt__(self, other):
        if value.index(self.x) == value.index(other.x):
            return suit1.index(self.y) < suit1.index(other.y)
        return value.index(self.x) < value.index(other.x)


class Deck:
    def __init__(self):
        self.deck_zero = []
        for i in suit1:
            for o in value:
                self.deck_zero.append(Card(o, i))

    def __getitem__(self, item):
        return self.deck_zero[item]

    def __len__(self):
        return len(self.deck_zero)

    def __str__(self):
        return f'deck[{len(self.deck_zero)}]:{",".join(str(k) for k in self.deck_zero)}'

    def shuffle(self):
        return random.shuffle(self.deck_zero)

    def draw(self, other):
        tmp = self.deck_zero[:other]
        self.deck_zero = self.deck_zero[other:]
        return tmp


class Player:
    def __init__(self, number):
        self.hand = []
        self.number = number

    def __str__(self):
        return f'player{self.number}\'s hand[{len(self.hand)}]:{",".join(str(i) for i in self.hand)}'


class Game:
    def __init__(self, first_player, second_player, new_deck):
        self.first_player = first_player
        self.second_player = second_player
        self.new_deck = new_deck
        self.new_deck.shuffle()
        self.table = []

    def print_table(self):
        return f'{" ".join(str(i) for i in self.table)}'

    def attack(self):  # first_player attacks
        c = self.first_player.hand.pop(0)
        self.table.append(c)
        print(f'player{self.first_player.number} attacks:{self.print_table()}')

    def defend(self):  # second_player defends
        for i in range(len(self.second_player.hand)):
            if self.table[-1].y == self.second_player.hand[i].y and self.table[-1] < self.second_player.hand[i]:
                tmp_c = self.second_player.hand.pop(i)
                self.table.append(tmp_c)
                print(
                    f'player{self.second_player.number} defends:{self.print_table()[:-3]} <-{self.print_table()[-3:]}')
                return True
        return False

    def addcardtotable2(self):  # adding single card to the defender's hand
        for i in self.table:
            for j in self.first_player.hand:
                if i.x == j.x:
                    x1 = self.first_player.hand.pop(self.first_player.hand.index(j))
                    self.table.append(x1)
                    print(
                        f'player{self.first_player.number} adds cards to table:{self.print_table()[-3:]} -> {self.print_table()[:-3]}')
                    # print(f'player{self.first_player.number} adds cards to table:{self.print_table()}')
                    return True
        return False

    def addcardtotable3(self):  # adding all available cards to the defender's hand
        for i in self.table:
            for j in self.first_player.hand:
                if i.x == j.x:
                    # print(i.x)
                    x1 = self.first_player.hand.pop(self.first_player.hand.index(j))
                    self.table.append(x1)
                    print(
                        f'player{self.first_player.number} adds cards to table:{self.print_table()[-3:]} -> {self.print_table()[:-3]}')

    def takecardsfromtable(self):  # if second_player can't defend, he takes all cards from table
        print(f'player{self.second_player.number} takes cards:{self.print_table()}')
        self.second_player.hand.extend(self.table)
        self.table = []
        # print(f'table_after_card_taken:{self.print_table()}')
        self.second_player.hand = sorted(self.second_player.hand)

    def player_switch(self):  # players switch sides
        # print('...switching sides...')
        self.first_player, self.second_player = self.second_player, self.first_player
        # print(f'sw {self.first_player}')
        # print(f'sw {self.second_player}')

    def takingcardsfromdeck(self):  # players take cards from deck to hand till they have 10
        print('taking cards')
        if len(self.first_player.hand) < 10:
            x = self.new_deck.draw(10 - len(self.first_player.hand))
            self.first_player.hand.extend(x)
            self.first_player.hand = sorted(self.first_player.hand)

        if len(self.second_player.hand) < 10:
            x = self.new_deck.draw(10 - len(self.second_player.hand))
            self.second_player.hand.extend(x)
            self.second_player.hand = sorted(self.second_player.hand)

        print(self.first_player)
        print(self.second_player)

    def round_start(self):  # players take 10 cards from deck at the start of the game
        print(self.new_deck)
        if not self.first_player.hand:
            self.first_player.hand = sorted(self.new_deck.draw(10))
        if not self.second_player.hand:
            self.second_player.hand = sorted(self.new_deck.draw(10))

    def action(self):  # clears table at the start of the round and main actions
        print(self.new_deck)
        self.table = []
        print(f'table:{self.print_table()}')

        print(self.first_player)
        print(self.second_player)

        self.attack()
        if self.defend():
            self.addcardtotable2()
        else:
            print(f'player{self.second_player.number} can\'t defend')
            self.addcardtotable3()
            self.takecardsfromtable()
            self.player_switch()  # same as in line 170

        while len(self.table) > 2:
            if self.defend():
                if self.addcardtotable2():
                    continue
                else:
                    # self.player_switch()  # if written this way, player.switch works only if self.addcardtotable2 activated
                    break


            else:
                print(f'player{self.second_player.number} can\'t defend')
                self.addcardtotable3()
                self.takecardsfromtable()
                self.player_switch()  # switching places back, because if player takes cards from table he can't attack next turn
                break

        print('...action_ends...')
        print(self.first_player)
        print(self.second_player)

    def round(self):
        self.round_start()
        while self.new_deck or self.first_player.hand != [] and self.second_player.hand != []:
            print('-' * 20, 'ROUND STARTS', '-' * 20)
            self.action()
            # if self.new_deck != []:   ????????????????????????
            #     self.takingcardsfromdeck()
            # elif self.new_deck == []:
            #     continue
            self.takingcardsfromdeck()
            self.player_switch()
            print('-' * 21, 'ROUND ENDS', '-' * 21)
        if len(self.first_player.hand) < len(self.second_player.hand):
            print(f'player{self.first_player.number} won')
        else:
            print(f'player{self.second_player.number} won')


deck = Deck()

player1 = Player(1)
player2 = Player(2)

game1 = Game(player1, player2, deck)

game1.round()
