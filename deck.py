import random

class Card():
    """ Class cards is created to print out right format.  
    The __inn__ uses dictionary for Ace,Joger,Queen and a King,  We use funtion type to find, not in, and boolian to figure out wrong inputs.   
    If there is not right input the program prints 'blk'
    Function is_blank uses boolean False/True to return those values. """
    
    def __init__(self, rank = "0", suit = ""):
        rank_dict = {"1":"A","11":"J","12":"Q","13":"K"}  
        if(type(rank) == str):
            if rank in '111213':
                rank = int(rank)

        if(type(rank) == int):
            if rank >= 1 and rank <= 13:
                if rank >= 2 and rank <= 10:
                    rank = str(rank)
                elif str(rank) in rank_dict:
                    rank = str(rank)
                    rank = rank_dict[rank]

        if rank not in '12345678910111213aAjJqQkK':
            rank = "blk"

        if type(suit) == int or suit not in "SDHCsdhc":
            suit = "blk"
        
        if rank == "" or suit == "":
            rank = "blk"
            suit = "blk"

        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.rank != "blk" and self.suit != "blk" or self.is_blank() == False:
            return "{:>2}{}".format(self.rank.upper(),self.suit.upper())
        else:
            return "{}".format("blk")

    def is_blank(self):
        if self.rank == "" or self.suit == "":
            return False
        else:
            return True

class Deck():
    """ The __init__ in deck creates 4 times cards of 13 and assigens suits to each of them.  
        The __init__ calls on class Card() for right presentation and delivers a deck
        The __str__ prints out all the deck in four lines.  Note, not the playing hand.  They playing hand is in class Playinghand()"""

    def __init__(self):
        deck = []
        suits = "shdc"     #the four suits Spade, Heart, Diamong and Club
        for card in range(1,14):
            for suit in suits:    
                card_name = str(Card(str(card),suit)).strip()
                deck.append(card_name)
        self.deck = deck
    
    def __str__(self):
        printed = ""
        deck_of_thirteen = [self.deck[x:x+13] for x in range(0, len(self.deck), 13)]
        for thirteen in deck_of_thirteen:
            printed += ("{:>3} "*len(thirteen)).format(*thirteen) + "\n"
        return printed.rstrip()
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop(0)

class PlayingHand():
    """ _init__ The playing hand constist tobegin with with 52 blanks or undealed cards.
        def add_card call on the class Deck that delivers def deal() that is pooped of the dect as dealed    """

    NUMBER_CARDS = 13   # 4 * 13 = 52 card deck

    def __init__(self):
        hand = ["blk" for line in range(self.NUMBER_CARDS)]
        self.hand = hand
    
    def __str__(self):
        printed = ("{:>3} "*len(self.hand)).format(*self.hand)
        self.hand = []
        return printed
    
    def add_card(self, card):
        self.hand.append(card)

def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)

def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    for i in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())
        
def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)
    deal_4_hands(deck, hand1, hand2, hand3, hand4)
    print("The 4 hands after dealing:")
    print_4_hands(hand1, hand2, hand3, hand4)

#The main program starts here
random.seed(10)
test_cards()

deck = Deck()
deck.shuffle()

print("The deck:")
print(deck)

test_hands(deck)
print("The deck after dealing:")
print(deck)