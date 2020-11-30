"""ZarzadzaniePortfelemProjektow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView

#from pages.views import export_view
from pages_.views import GameView, ResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('export.csv', export_view, name="export_to_csv"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('game/', GameView.as_view(), name='game-main'),
    path('results/', ResultsView.as_view(), name='game-results'),
    path('api/', include('engine_refactored.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
