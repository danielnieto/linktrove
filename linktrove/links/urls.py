from django.urls import path
from .views import LinkListView, LinkCreateView, LinkUpdateView, LinkDetailView


urlpatterns = [
    path("", LinkListView.as_view(), name="link_list"),
    path("new", LinkCreateView.as_view(), name="link_create"),
    path("update/<str:pk>", LinkUpdateView.as_view(), name="link_update"),
    path("detail/<str:pk>", LinkDetailView.as_view(), name="link_detail"),
]
