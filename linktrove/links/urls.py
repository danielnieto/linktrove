from django.urls import path
from .views import (
    LinkListView,
    LinkCreateView,
    LinkUpdateView,
    LinkDetailView,
    LinkDeleteView,
    LinkDeleteConfirmView,
)


urlpatterns = [
    path("", LinkListView.as_view(), name="link_list"),
    path("new", LinkCreateView.as_view(), name="link_create"),
    path("update/<str:pk>", LinkUpdateView.as_view(), name="link_update"),
    path("detail/<str:pk>", LinkDetailView.as_view(), name="link_detail"),
    path("delete/<str:pk>", LinkDeleteView.as_view(), name="link_delete"),
    path(
        "delete-confirm/<str:pk>",
        LinkDeleteConfirmView.as_view(),
        name="link_delete_confirm",
    ),
]
