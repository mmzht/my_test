import random


##class Cards:
##
##    def __init__(self):
##        self.suits = ["C","D","H","S"]
##        self.ranks = ["A","2","3","4",
##                      "5","6","7","8",
##                      "9","10","J","Q","K"]
##        self.jokers = ["Red Joker","Black Joker"]
##        self.deck = []
##
##    def make_deck(self,include_jokers=True):
##        self.deck=[s + r for s in self.suits for r in self.ranks]
##        if include_jokers:
##            self.deck += self.jokers
##        random.shuffle(self.deck)
##
##    def deal_cards(self):
##        card = self.deck.pop()
##        return card
    
def make_deck(include_jokers=True):
    suits = ["C","D","H","S"]
    ranks = ["A","2","3","4",
             "5","6","7","8",
             "9","10","J","Q","K"]
    deck = [s + r for s in suits for r in ranks]
    if include_jokers:
        deck += ["Red Joker","Black Joker"]
    random.shuffle(deck)
    return deck

def hide_three(deck):
    hiden = random.sample(deck,3)
    for card in hiden:
        deck.remove(card)
    return hiden,deck
    
def deal_cards(deck):
    p1 = deck[::3]
    p2 = deck[1::3]
    p3 = deck[2::3]
    return p1,p2,p3


        
        
        
        
        
