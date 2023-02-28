from django import forms

from . import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["user", "headline", "body", "rating"]
        exclude = ("time_created", )
        labels = {"user": "Utilisateur", "headline": "Titre", "body": "Commentaire", "rating": "Note"}
        """
        widgets = {"headline": forms.TextInput(attrs={"placeholder": "Titre", "label": ""}),
                   "body": forms.Textarea(attrs={"placeholder": "Commentaire", "label": ""}),
                   }
        """
