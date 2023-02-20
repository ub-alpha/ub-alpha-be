from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberView.as_view()),
    path('/<int:pk>', views.MemberDetailView.as_view()),
]