from django.http import HttpResponse
from django.views.generic import TemplateView

from engine_refactored.models import CompleteGame
from engine_refactored import engine

from json import dumps

class GameView(TemplateView):
    template_name = 'game/main.html'
    
    def get_context_data(self, **kwargs):
       return super().get_context_data(**kwargs) # ??? It was in legacy version, so idk.

class ResultsView(TemplateView):
    template_name = 'results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = self.restore_history()

        return context
    
    @staticmethod
    def convert_round_to_dictionary(game): #CompleteGame
        result = {}
        result['start_date'] = game.game_info.parent_game.start_date.strftime("%Y-%m-%d %H:%M:%S")
        result['end_date'] = game.end_date.strftime("%Y-%m-%d %H:%M:%S")
        projects = engine.game_to_projects(game.game_info.parent_game.project_generation_seed)
        combinations = engine.projects_to_wallets(projects)
        ratings = engine.projects_to_ratings(projects, wallets, game.wallet_final_score_seed)
        player_choice = game.game_info.chosen_set_index
        player_chosen_indices = combinations[player_choice]
        player_rating = ratings[player_choice]
       
        for (fmt_string, attr_name) in [('%d', 'cost'), ('%.2f', 'risk'), ('%d', 'expected_profit'), ('%.3f', 'expected_return'),
            ('%d', 'real_profit'), ('%.3f', 'real_return')]:
            result[attr_name] = fmt_string % getattr(r, attr_name)

        return result
 
    def restore_history(self):
        user_pk = self.request.user.pk
        user_rounds = CompleteGame.objects.filter(game_info__parent_game__user_id=user_pk).order_by('-start_date')
        serialized = list(map(convert_round_to_dictionary, r))
            
        return serialized
#TODO: remove
class PostTemplateView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest('Bad GET request!')

    def post(self, request, *args, **kwargs):
        self.map_variables(request)

        context = self.get_context_data()
        rendered = self.render_to_response(context)
        return rendered

    def map_variables(self, request):
        p = dict(request.POST)

        prohibited_keys = []
        if hasattr(self, 'checkbox_name'):
            prohibited_keys.append(self.checkbox_name)
        if hasattr(self, 'projects_list'):
            prohibited_keys.append(self.projects_list)

        for key in p.keys():
            if type(p[key]) is list:
                if key in prohibited_keys:
                    continue
                p[key] = p[key][0]

        self.post = p
        return p

class InitGame(PostTemplateView):
    # this class creates game object and round 1
    template_name = "game/init_game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            g = Game(self.request.user)
            g.save()

            options = engine_refactored.game_to_projects(g.id)
            context['game_id'] = g.id
            context['options'] = dumps(options)
            context['image'] = bytes()

            return context


class RoundSubmit(PostTemplateView):
    # this class is finishing the round
    template_name = "game/submit_round.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.request.user.is_authenticated:
            return None
        
        choices = loads(self.post['choices'])
        if len(choices) != settings.WALLET_SIZE:
            return context

        if any([project_id >= settings.PROJECT_COUNT for project_id in choices]):
            return context

        game_id = self.post['game_id']
        try:
            game = Game.objects.get(id=game_id)
        except ObjectDoesNotExist:
            return context
        projects = engine.game_to_projects(game_id)
        choice_idx = engine.projects_to_wallets(len(projects)).index(choices)
        item = PlayerChoice(game, choice_idx)
        item.save()
        project_ratings = engine.projects_to_ratings(projects, item.id)
        
        return context


