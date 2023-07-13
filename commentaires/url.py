from re import I
from django.urls import path
from rest_framework.views import APIView
from . import views
from .views import CommentaireApi,CommentairEditeApi,CommentaireFiltreApi
from rest_framework.authtoken import views


urlpatterns = [
    path('commentaires/', CommentaireApi.as_view()),
    path('commentaires/<str:id>', CommentairEditeApi.as_view()),
    path('commentaires/filter/', CommentaireFiltreApi.as_view()),
]