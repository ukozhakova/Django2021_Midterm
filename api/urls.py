from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    path('books/<int:pk>/', views.BookRetrieveAPIView.as_view()),
    path('journals/', views.JournalAPIView.as_view()),
    path('journals/<int:pk>/', views.JournalRetrieveAPIView.as_view())
]

