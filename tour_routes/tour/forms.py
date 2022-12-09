from django import forms
from .models import SightReview

# Atsiliepimo formos formavimas
class SightReviewForm(forms.ModelForm):
    class Meta:
        model = SightReview
        field = ('content', 'sight','reviewer' )
        widgets = {
            'sight': forms.HiddenInput(),
            'reviewer': forms.HiddenInput(),
        }

        