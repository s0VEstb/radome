from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('about_me/', views.about_me),
    path('about_friend/', views.about_friend),
    path('datetime_now/', views.datetime_now),
    path('books_list/', views.BooksListView.as_view(), name='books_list'),
    path('books_list/<int:id>/', views.BooksDetailView.as_view(), name='books_detail'),
    path('books_create/', views.BooksCreateView.as_view()),
    path('books_list/<int:id>/update/', views.BooksUpdateView.as_view()),
    path('books_list/<int:id>/delete/', views.BooksDeleteView.as_view(), name='books_delete'),
]