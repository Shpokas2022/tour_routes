from django import forms
from .models import SightReview


class SightReviewForm(forms.ModelForm):
    class Meta:
        model = SightReview
        field = ('content', 'sight','reviewer' )
        widgets = {
            'sight': forms.HiddenInput(),
            'reviewer': forms.HiddenInput(),
        }

        