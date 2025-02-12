from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('data/', views.data_saved, name="data_saved"),
    path('congratulations/', views.congratulations, name="congratulations"),
]