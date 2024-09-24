from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('cloth_list/', views.ClothListView.as_view()),
]