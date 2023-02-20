from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterListView.as_view()),
]