import random

class Card:
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number

    def __str__(self):
        print(number, "of", suit)

class Hand:
    def __init__(self,hand):
        self.hand = hand

    def count(self):
        count = 0
        for card in hand_list:
            count += int(card.number)
        return count

    def empty():
        self.hand = 0

class Deck:
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    numbers = [str(num) for num in range(1,14)]
    def __init__(self):
        self.cards = []
        for suit in suits:
            for number in numbers:
                self.cards.append(card(suit,number))

    def shuffle(self):
        random.shuffle(self.cards)

    def refresh(self):
        for suit in suits:
            for number in numbers:
                self.cards.append(card(suit,number))

    def deal(self):
        return self.cards.pop()

    

    
