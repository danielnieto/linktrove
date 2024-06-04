from django import forms
from .models import Link
from .widgets import TagsWidget, URLWidget


class LinkCreateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["url", "notes", "tags"]

        widgets = {
            "url": URLWidget(),
            "tags": TagsWidget(),
        }

    def clean_url(self):
        # remove trailing slashes
        return self.cleaned_data.get("url", "").rstrip("/")


class LinkUpdateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["notes", "tags"]

        widgets = {
            "tags": TagsWidget(),
        }
