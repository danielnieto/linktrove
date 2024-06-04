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
            "notes": forms.Textarea(
                attrs={
                    "class": "textarea leading-normal textarea-bordered w-full my-1 px-2"
                }
            ),
            "tags": TagsWidget(
                attrs={"class": "input input-bordered w-full my-1 px-2"}
            ),
        }
