from django.urls import path
from .views import import_articles

urlpatterns = [
    path('',import_articles)
]