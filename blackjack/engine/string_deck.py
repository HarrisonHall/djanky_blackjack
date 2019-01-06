import random

class Card:
    def __init__(self,number):
        self.number = number

    def __str__(self):
        print(str(self.number))

class Hand:
    def __init__(self,hand):
        self.hand = hand

    def count(self):
        count = 0
        for card in hand:
            count += int(card.number)
        return count

    def add(self,card):
        self.hand += " " + card

    def empty():
        self.hand = 0

class Deck:
    numbers = [str(num) for num in range(1,14)]
    def __init__(self):
        self.cards = []
        for x in range(4):
            for number in numbers:
                self.cards.append(card(suit,number))

    def shuffle(self):
        random.shuffle(self.cards)

    def refresh(self):
        for x in range(4):
            for number in numbers:
                self.cards.append(card(suit,number))

    def deal(self):
        return self.cards.pop()

    

    
