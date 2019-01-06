from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
from blackjack.models import Game, Player, MultiplayerGame
from django.http import HttpResponse
import requests
from blackjack.form.forms import GameForm, HitForm, CreateMultiplayerForm, JoinMultiplayerForm

class JoinBlackjackCreateView(CreateView):
    form_class = GameForm
    template_name = 'join.html'
    #html = template.render(context=locals(), request=request)

    def __init__(self):
        super().__init__()
        
    def get(self , request):
        name = self.request.GET.get("name","Your Name Here")
        get_response = super().get(request)
        return get_response

    def get_initial(self, **kwargs):
        initial_form = super().get_initial(**kwargs)
        initial_form['name'] = self.request.GET.get("name","you")
        #initial_form['url'] = self.image_url
        return initial_form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['name'] = self.image_url
        #context['name'] = name
        return context

class JoinBlackjackUpdateView(UpdateView):
    form_class = HitForm
    model = Game
    template_name = 'play.html'

    def get_object(self, queryset=None):
        print(self.kwargs)
        obj = Game.objects.get(id=self.kwargs['pk'])
        # Update State
        if (obj.hit):
            obj.deal()
        else:
            obj.refresh()
            obj.shuffle()
            if ("Hello" not in obj.name):
                obj.name = "Hello, " + obj.name
        
        if (obj.count() > 21):
            obj.name = "LOSER"
        elif (obj.count() == 21):
            obj.name = "WINNER"
            
        return obj

class JoinBlackjackMultiplayerCreateView(CreateView):
    form_class = CreateMultiplayerForm
    template_name = 'createmultiplayer.html'

    def __init__(self):
        super().__init__()
        
    def get(self , request):
        name = self.request.GET.get("name","Your Name Here")
        get_response = super().get(request)
        return get_response

    def get_initial(self, **kwargs):
        initial_form = super().get_initial(**kwargs)
        initial_form['name'] = self.request.GET.get("name","")
        #initial_form['url'] = self.image_url
        return initial_form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['name'] = self.image_url
        #context['name'] = name
        return context

class JoinBlackjackMultiplayerCodeTemplateView(TemplateView):
    template_name = "code.html"

class JoinBlackjackMultiplayerSingleCreateView(CreateView):
    form_class = JoinMultiplayerForm
    template_name = 'joinmultiplayer.html'

    def __init__(self):
        super().__init__()
        
    def get(self , request):
        name = self.request.GET.get("name","")
        get_response = super().get(request)
        return get_response

    def get_initial(self, **kwargs):
        initial_form = super().get_initial(**kwargs)
        initial_form['name'] = self.request.GET.get("name","")
        initial_form['room'] = self.request.GET.get("room","")
        #initial_form['url'] = self.image_url
        return initial_form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['name'] = self.image_url
        #context['name'] = name
        return context

def all_lost(room,player):
    ids = [int(pkid) for pkid in room.players.split()]
    for pkid in ids:
        p = Player.objects.get(id=pkid)
        if p.hit != True and p.score() < 21:
            print("All did not lose")
            return False
    print("All lost")
    return True

def add_players_to_dict(room):
    all_scores = {}
    ids = [int(pkid) for pkid in room.players.split()]
    for pkid in ids:
        p = Player.objects.get(id=pkid)
        all_scores[str(pkid)] = [p.name, p.score()]
    return all_scores

    
def PlayBlackjackMultiplayerTemplateView(request, pk):
    p = Player.objects.get(id=pk)
    r = MultiplayerGame.objects.get(id=p.room)
    values = {'pk':pk,
              'reload':False,
              'ready' : True,
              'score': 0,
              'play' : False,
              'win' : False,
              'lose' : False,
              'name' : p.name,
              'yikes' : False,
              'room' : p.room,
              'all_scores' : {},
              'wait' : False,
              'finished' : False,
    }
    
    # POST
    if (request.method == "POST"):
        # It was hit!
        hit = request.POST.get('is_hit','off') == 'on'
        if (hit):
            p.hand += r.deal()
            p.count = p.score()
            values['score'] = p.count
        else:
            p.hit = True
        p.save()
        r.save()
        if (p.score() > 21):
            p.hit = True
            p.save()
            values['yikes'] = True
            values['lose'] = True
            values['reload'] = True
            return render(request, "multiplayer.html", values)
        elif (p.score() == 21 or p.hit):
            values['wait'] = True
            p.hit = True
            p.save()
            values['reload'] = True
            return render(request, "multiplayer.html", values)
        else:
            return render(request, "multiplayer.html", values)
    
    # GET
    else: 
        if (r.total_players() < r.num_players):
            r.add_player(pk)
            if (r.total_players() == r.num_players):
                r.refresh()
            values['score'] = p.score()
            values['reload'] = True
            values['ready'] = False
            r.save()
            return render(request, "multiplayer.html", values)
        else:
            if (p.count > 21):
                if (all_lost(r,p)):
                    # All have lost, load scores
                    values['lose'] = True
                    print()
                    values['all_scores'] = add_players_to_dict(r)
                    print([p.name, p.score()])
                    print(values['all_scores'])
                    values['finished'] = True
                    values['wait'] = True
                    return render(request, "multiplayer.html", values)
                else:
                    values['all_scores'] = add_players_to_dict(r)
                    print([p.name, p.score()])
                    print(values['all_scores'])
                    values['lose'] = True
                    values['reload'] = True
                    values['score'] = p.score()
                    values['finished'] = True
                    return render(request, "multiplayer.html", values)
            elif (p.hit == True):
                values['all_scores'] = add_players_to_dict(r)
                print([p.name, p.score()])
                print(values['all_scores'])
                values['lose'] = True
                values['reload'] = True
                values['wait'] = True
                values['score'] = p.score()
                values['finished'] = True
                return render(request, "multiplayer.html", values)
            else:
                return render(request, "multiplayer.html", values)
