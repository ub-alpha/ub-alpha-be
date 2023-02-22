from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberRegisterView.as_view()),
    path('/spacename', views.MemberDetailView.as_view()),
    path('/<int:pk>/point', views.MemberPointView.as_view()),
]