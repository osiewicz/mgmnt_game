from datetime import datetime 

from django.conf import settings
from django.db import models
from django.utils import timezone

# Attributes in app are "lazy" - Game stores only seed that can be used
# to reproduce available wallets and their properties - and also to get a final score for each wallet.
class Game(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='games')
    start_date = models.DateTimeField(auto_now_add=True)

class CompleteGame(models.Model):
    parent_game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='choice', primary_key=True)
    # Index of chosen wallet (set of projects)
    chosen_set_index = models.IntegerField()
    end_date = models.DateTimeField(auto_now_add=True)
