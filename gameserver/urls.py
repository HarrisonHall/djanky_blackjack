"""gameserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blackjack import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Singleplayer
    path('blackjack/join', views.JoinBlackjackCreateView.as_view(), name="blackjack_game_create"),
    path('blackjack/play/<int:pk>', views.JoinBlackjackUpdateView.as_view(), name="blackjack_game_update"),

    # Multiplayer
    path('blackjack/createmultiplayer', views.JoinBlackjackMultiplayerCreateView.as_view(), name="blackjack_multiplayer_create"),
    path('blackjack/code/<int:pk>', views.JoinBlackjackMultiplayerCodeTemplateView.as_view(), name="blackjack_multiplayer_code"),
    path('blackjack/joinmultiplayer', views.JoinBlackjackMultiplayerSingleCreateView.as_view(), name="blackjack_joinmultiplayergame"),
    path('blackjack/playmultiplayer/<int:pk>', views.PlayBlackjackMultiplayerTemplateView, name="blackjack_multiplayergame"),

    # Base
    path('', views.JoinBlackjackCreateView.as_view(), name="blackjack_game_create"),
    path('blackjack', views.JoinBlackjackCreateView.as_view(), name="blackjack_game_create"),
]
