from django import forms
from .models import Link


class LinkCreateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["url", "notes"]

        widgets = {
            "url": forms.URLInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "onblur": "if (!~this.value.indexOf('http')) this.value = 'https://' + this.value",
                }
            ),
            "notes": forms.Textarea(
                attrs={"class": "textarea textarea-bordered w-full"}
            ),
        }
