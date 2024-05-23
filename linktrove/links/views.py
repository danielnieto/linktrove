from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from linktrove.links.services import extract_metadata
from .models import Link
from .forms import LinkCreateForm


class LinkListView(LoginRequiredMixin, ListView):
    model = Link
    context_object_name = "links"
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return Link.objects.filter(user=user).order_by("-created")


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    form_class = LinkCreateForm
    template_name = "links/link_create.html"
    success_url = reverse_lazy("link_list")

    def form_valid(self, form):
        form.instance.user = self.request.user

        url = form.cleaned_data["url"]
        title, description, thumbnail, favicon = extract_metadata(url)

        form.instance.title = title
        form.instance.description = description
        form.instance.thumbnail = thumbnail
        form.instance.favicon = favicon

        return super().form_valid(form)


class LinkUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "links/partials/_link_update.html"
    model = Link
    fields = ["notes"]

    def get_success_url(self):
        return reverse_lazy("link_detail", kwargs={"pk": self.object.id})


class LinkDetailView(LoginRequiredMixin, DetailView):
    template_name = "links/partials/_link_detail.html"
    model = Link
