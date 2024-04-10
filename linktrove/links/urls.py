from django.urls import path
from .views import LinksListView


urlpatterns = [
    path("", LinksListView.as_view()),
]
