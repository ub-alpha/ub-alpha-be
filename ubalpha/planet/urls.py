from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlanetListView.as_view()),
]