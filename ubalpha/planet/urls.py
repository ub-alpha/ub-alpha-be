from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlanetListView.as_view()),
    path('/detail', views.DetailCreateView.as_view()),
    path('/detail/<int:pk>/point', views.DetailView.as_view()),
    path('/detail/<int:pk>', views.DetailCouponView.as_view()),
]