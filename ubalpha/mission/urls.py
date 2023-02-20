from django.urls import path
from . import views

urlpatterns = [
    path('', views.MissionListView.as_view()),
]