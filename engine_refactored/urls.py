from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from pages_ import *

urlpatterns = [
    path('init/', views.InitGame.as_view(), name='api-init-game'),
    path('submit/', views.RoundSubmit.as_view(), name='api-submit-round'),
]
