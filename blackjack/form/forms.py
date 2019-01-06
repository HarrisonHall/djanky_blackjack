from django import forms
from blackjack.models import Game, MultiplayerGame, Player

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name']

class HitForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['hit']

class CreateMultiplayerForm(forms.ModelForm):
    class Meta:
        model = MultiplayerGame
        fields = ['num_players']

class JoinMultiplayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name','room']

