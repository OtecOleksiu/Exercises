import random

value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
value1 = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
          'Q': 10, 'K': 10, 'A': 11}
suit = {'S': '♠', 'C': '♣', 'D': '♦', 'H': '♥'}
suit1 = ('S', 'C', 'D', 'H')


class Card:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}{suit[self.y]}'

    def __gt__(self, other):
        return value1[self.x] > other

    def __lt__(self, other):
        return value1[self.x] < other

    def __eq__(self, other):
        return value1[self.x] == other

    def __add__(self, other):
        if type(other) is int:
            return value1[self.x] + other
        else:
            return value1[self.x] + value1[other.x]

    def __radd__(self, other):
        if type(other) is int:
            return value1[self.x] + other
        else:
            return value1[self.x] + value1[other.x]


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

    def draw(self):
        t = self.deck_zero.pop(0)
        return t


class Player:
    def __init__(self, number):
        self.hand = []
        self.number = number

    def __str__(self):
        if self.number == 2:
            return f'dealer\'s hand[{sum(self.hand)}]:{",".join(str(i) for i in self.hand)}'
        return f'player\'s hand[{sum(self.hand)}]:{",".join(str(i) for i in self.hand)}'


class Game:
    def __init__(self, first_player, dealer, new_deck):
        self.first_player = first_player
        self.dealer = dealer
        self.new_deck = new_deck
        self.new_deck.shuffle()

    def card_deal(self):
        x = input('would you like to take a card? Y/N\n')
        if x in ['y', 'Y', 'n', 'N']:
            if x == ('Y' and 'y'):
                self.first_player.hand.append(self.new_deck.draw())
                print(self.first_player)
                if sum(self.first_player.hand) < 21:
                    self.card_deal()
                elif sum(self.first_player.hand) == 21:
                    print('player won')

                else:
                    print('BUSTED')

            else:
                self.dealer_plays()

        else:
            print('Please answer Y or N')
            self.card_deal()

    def dealer_cards_hidden(self):
        return '|*|' * (len(self.dealer.hand) - 1)

    def dealer_plays(self):
        while sum(self.dealer.hand) < 17:

            self.dealer.hand.append(self.new_deck.draw())
            if sum(self.dealer.hand) > 21:
                print(self.dealer)
                print('dealer busted')
                break
            print(self.dealer)

    def round(self):

        self.dealer.hand.append(self.new_deck.draw())
        self.dealer.hand.append(self.new_deck.draw())

        print(f'dealer\'s hand[{value1[self.dealer.hand[0].x]}]: {self.dealer.hand[0]},{self.dealer_cards_hidden()}')
        self.first_player.hand.append(self.new_deck.draw())
        self.first_player.hand.append(self.new_deck.draw())
        print(self.first_player)
        if sum(self.first_player.hand) == 21 and sum(self.dealer.hand) != 21:
            print('BLACKJACK')
        elif sum(self.first_player.hand) == 21 and sum(self.dealer.hand) == 21:
            print('push')
        else:
            if sum(self.first_player.hand) < 21:
                self.card_deal()

        print('-' * 35)
        if sum(self.first_player.hand) < 21 and sum(self.dealer.hand) <= 21:
            print(self.first_player)
            print(self.dealer)
            if sum(self.first_player.hand) > sum(self.dealer.hand):
                print(f'player won by points {sum(self.first_player.hand)} vs {sum(self.dealer.hand)}')
            elif sum(self.first_player.hand) == sum(self.dealer.hand):
                print('push by points')
            else:
                print(f'dealer won by points {sum(self.dealer.hand)} vs {sum(self.first_player.hand)}')


deck1 = Deck()

deck1.shuffle()

player = Player(1)
dealer = Player(2)

game = Game(player, dealer, deck1)

game.round()
