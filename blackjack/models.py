from django.db import models
from django.urls import reverse_lazy
import random

class Game(models.Model):
    name = models.TextField()
    deck = models.TextField()
    hand = models.TextField()
    hit = models.BooleanField(default='False')

    def __str__(self):
        return str(self.count())

    def refresh(self):
        self.deck = ""
        self.hand = ""
        for x in range(4):
            for number in range(1,13):
                self.deck += str(number) + " "
                
    def count(self):
        nums = [int(s) for s in self.hand.split() if s.isdigit()]
        count = sum(nums)
        return count

    def deal(self):
        nums = [int(s) for s in self.deck.split() if s.isdigit()]
        self.hand += str(nums.pop()) + " "
        self.deck = ""
        for num in nums:
            self.deck += str(num) + " "

    def empty():
        self.hand = ""

    def shuffle(self):
        nums = [int(s) for s in self.deck.split() if s.isdigit()]
        random.shuffle(nums)
        self.deck = ""
        for num in nums:
            self.deck += str(num) + " "

    def get_absolute_url(self):
        return reverse_lazy("blackjack_game_update", args=[str(self.id)])

class MultiplayerGame(models.Model):
    deck = models.TextField()
    all_players_played = models.BooleanField(default='False')
    game_over = models.BooleanField(default='True')
    players = models.TextField()
    num_players = models.IntegerField()

    def __str__(self):
        return str(num_players)

    def refresh(self):
        self.deck = ""
        self.hand = ""
        for x in range(4):
            for number in range(1,13):
                self.deck += str(number) + " "
                
    def deal(self):
        try:
            nums = [int(s) for s in self.deck.split() if s.isdigit()]
            hand = str(nums.pop()) + " "
            self.deck = ""
            for num in nums:
                self.deck += str(num) + " "
            return hand
        except:
            self.refresh()
            nums = [int(s) for s in self.deck.split() if s.isdigit()]
            hand = str(nums.pop()) + " "
            self.deck = ""
            for num in nums:
                self.deck += str(num) + " "
            return hand

    def shuffle(self):
        nums = [int(s) for s in self.deck.split() if s.isdigit()]
        random.shuffle(nums)
        self.deck = ""
        for num in nums:
            self.deck += str(num) + " "

    def add_player(self, playerid):
        splayers = [p for p in self.players.split()]
        if str(playerid) not in splayers:
            self.players += str(playerid) + " "

    def total_players(self):
        return len([p for p in self.players.split()])

    def get_absolute_url(self):
        return reverse_lazy("blackjack_multiplayer_code", args=[str(self.id)])

class Player(models.Model):
    name = models.TextField()
    hit = models.BooleanField(default='False')
    hand = models.TextField()
    count = models.IntegerField(default='0')
    room = models.IntegerField()

    def __str__(self):
        return "Player is: " + str(self.id)

    def get_absolute_url(self):
        return reverse_lazy("blackjack_multiplayergame", args=[str(self.id)])

    def score(self):
        nums = [int(s) for s in self.hand.split() if s.isdigit()]
        count = sum(nums)
        self.count = count
        return count

    def empty(self):
        self.hand = ""
