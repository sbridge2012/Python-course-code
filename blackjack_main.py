#work in progress - not yet completed
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + "  of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    # def __str__(self):
    # return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):

        return self.deck.pop(0)


class Hand:
    def __init__(self, name):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces
        self.name = ""

    def add_card(self, new_card):

        self.cards.append(new_card)
        self.value += values[new_card.rank]
        if new_card.rank == 'Ace':
            self.aces += 1


    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -10
            self.aces -= 1
            print('value with ace', self.aces , self.value)

    def __str__(self):
        string = ' '
        for card in self.cards:
            string = string + ' ' + '\n' + str(card)
        return string


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self, winnings):
        self.total += self.bet

    def lose_bet(self, losses):
        self.total -= self.bet


class Player:

    def __init__(self, name):
        self.name = name


def show_hit():
    print('from show hit')


def take_bet(player_chips):

     while True:
        try:
            player_chips.bet= int(input("How many chips would you like to bet?"))
        except:ValueError
        else:
            if player_chips.bet > player_chips.total:
                print("Sorry you do not have enough chips to bet, you can bet up to", player_chips.total)
            else:
                break


# def hit(deck, hand):
# pass

def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    q=input("Would you like to hit or stand?")
    if q.lower().startswith('h'):
        print("cool")
        deal=deck.deal()
        hand.add_card(deal)



#  pass


def show_some(player,dealer):

    print('player one cards',*player.cards ,sep='\n')
    print('dealer cards', *dealer.cards, sep='\n')
    print( sep='\n')

   # print('player two cards' ,dealer.cards[0])
    print('player one value ',player_one.value)
    print('dealer value ' , player_two.value)

def show_all(player, dealer):

    print(*player.cards ,sep='\n')
    print(*dealer.cards, sep='\n')


def player_busts():

    if player_one.value > 21:

        return True
    elif player_two.value > 21:

        return True





# def player_wins():
# pass

# def dealer_busts():
# pass

# def dealer_wins():
#  pass

# def push():
# pass

game_on = True

player_one = Hand("Barry")
player_two = Hand("Dealer Russell")

while game_on:
    player_chips = Chips()
    take_bet(player_chips)

    print("player chips bet is ", player_chips.bet)

    deck = Deck()


    deck.shuffle()
    #card_one = deck.deal()
    #card_two = deck.deal()
    #card_three = deck.deal()
    #card_four = deck.deal()

    for x in range(2):
        p = deck.deal()
        s = deck.deal()
        player_one.add_card(p)
        player_two.add_card(s)

        if p.rank == 'Ace':
            print('ACE BOI')
            player_one.adjust_for_ace()


    #player_one.add_card(card_one)
    #player_one.add_card(card_two)
    #player_two.add_card(card_three)
    #player_two.add_card(card_four)




    show_some(player_one,player_two)

    busted = player_busts()

    #hit_or_stand(deck,player_one)
   # hit_or_stand(deck, player_two)

   #while playing:












# h=Hand()
# new_deck = Deck()

##card1=new_deck.deal()
# card2=new_deck.deal()
# card3=new_deck.deal()
# h.add_card(card1)
# h.add_card(card2)
# h.add_card(card3)
# print(h)



