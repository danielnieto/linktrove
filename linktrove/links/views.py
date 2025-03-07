from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from linktrove.links.services import extract_metadata
from .models import Link
from .forms import LinkCreateForm, LinkUpdateForm
from .mixins import OwnLinkQuerysetMixin, OwnTagQuerysetMixin
from django.http import HttpResponse
from django.db.models import Q
from taggit.models import Tag


class LinkListView(LoginRequiredMixin, OwnLinkQuerysetMixin, ListView):
    model = Link
    paginate_by = 5
    ordering = "-created"

    def get_template_names(self):
        if (
            "hx-request" in self.request.headers
            and "hx-history-restore-request" not in self.request.headers
        ):
            return ["links/partials/_link_list_and_pagination.html"]
        return super().get_template_names()

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("search")
        tags = self.request.GET.get("tags", "")

        if query:
            qs = qs.filter(
                Q(url__icontains=query)
                | Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(notes__icontains=query)
            )

        if tags:
            for tag in tags.split(","):
                qs = qs.filter(tags__name=tag.strip())

        return qs


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


class LinkUpdateView(LoginRequiredMixin, OwnLinkQuerysetMixin, UpdateView):
    template_name = "links/partials/_link_update.html"
    model = Link
    form_class = LinkUpdateForm

    def get_success_url(self):
        return reverse_lazy("link_detail", kwargs={"pk": self.object.id})


class LinkDetailView(LoginRequiredMixin, DetailView):
    template_name = "links/partials/_link_detail.html"
    model = Link


class LinkDeleteView(LoginRequiredMixin, OwnLinkQuerysetMixin, DeleteView):
    model = Link

    def get_success_url(self):
        return None

    def delete(self, *args, **kwargs):
        response = super().delete(*args, **kwargs)
        response.headers["HX-Trigger-After-Settle"] = "refresh-link-list"
        response.status_code = 200
        return response


class LinkDeleteConfirmView(LoginRequiredMixin, DetailView):
    model = Link
    template_name = "links/partials/_delete_confirmation_dialog.html"


def noop(request):
    return HttpResponse(request, "")


class TagListView(LoginRequiredMixin, OwnTagQuerysetMixin, ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "links/components/partials/_tag_list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        tags = self.request.GET.get("tags", "")

        if tags:
            exclude_tags = [tag.strip() for tag in tags.split(",")]
            qs = qs.exclude(name__in=exclude_tags)

        if query:
            qs = qs.filter(name__icontains=query)

        return qs
