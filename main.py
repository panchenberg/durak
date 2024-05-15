import random

# I don't see reason for class deck, so it will be a bunch of functions

#suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds']
values = ['2', '3', '4', '5']

deck = []


def dealing(deck):
    """
    deals 6 cards to the hand from the deck
    :param deck:
    :return: 6 cards hand
    """
    hand = []
    for i in range(0, 2):
        hand.append(deck.pop())
    return hand


def createNewDeck(deck):
    """
    creating a new set of cards for the game
    :return: list of objects Card
    """
    for i in range(0, len(suits)):
        for j in range(0, len(values)):
            deck.append(Card(i, j))

    random.shuffle(deck)
    trump_card = deck.pop()
    print(f"trump card is {trump_card}")
    trump = trump_card.suit
    deck.append(trump_card)
    return deck, trump


def compare(first, second, trump):

    if first.suit == second.suit:
        if first.value > second.value:
            print(f"{second.__str__()} not beat {first.__str__()}")
            return -1
        if first.value < second.value:
            print(f"{second.__str__()} beat {first.__str__()}")
            return 1
    elif first.suit == trump:
        print(f"{second.__str__()} not beat {first.__str__()}")
        return -1
    elif second.suit == trump:
        print(f"{second.__str__()} beat {first.__str__()}")
        return 1


class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        if value > 13:
            print('out of range')
            exit(-1)
        if suit > 3:
            print('out of range')
            exit(-1)

    def __str__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

    __repr__ = __str__

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


class Player:
    def __init__(self, hand):
        self.hand = hand

    def playCard(self):
        print(self.hand)
        print(f"what card do you want to play? (0-{len(self.hand)-1})")
        chosenIndex = int(input())
        chosenCard = self.hand.pop(chosenIndex)
        return chosenCard

    def takeCard(self):
        while len(self.hand) < 2:
            try:
                self.hand.append(deck.pop())
            except IndexError:
                print("Deck is empty")



deck = createNewDeck(deck)
trump = deck[1]
deck = deck[0]

player1 = Player(dealing(deck))
player2 = Player(dealing(deck))



def theGame(player1, player2):
    print("username1 your move") #TODO make username change
    card1 = player1.playCard()
    print("username2 your move")
    card2 = player2.playCard()
    result = compare(card1, card2, trump)
    print(result)
    if result == -1:
        player1.hand.append(card1)
        player2.hand.append(card2)
    else:
        player1.takeCard()
        player2.takeCard()
        theGame(player2, player1)
    theGame(player1, player2)

theGame(player1,player2)
