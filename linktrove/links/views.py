from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Link


class LinksListView(LoginRequiredMixin, ListView):
    model = Link
    context_object_name = "links"
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return Link.objects.filter(user=user)
