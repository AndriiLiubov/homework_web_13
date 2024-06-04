from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='main_paginate'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('tag/', views.tag, name='tag'),
    path('author_page/<fullname>', views.detail, name='author_page'),
]