from django import forms
from . models import Sight, SightReview

# Atsiliepimo formos formavimas
class SightReviewForm(forms.ModelForm):
    class Meta:
        model = SightReview
        fields = ('content', 'sight','reviewer' )
        widgets = {
            'sight': forms.HiddenInput(),
            'reviewer': forms.HiddenInput(),
        }


#  Užpildymo formos formavimas
class SightForm(forms.ModelForm):
    class Meta:
        model = Sight
        fields = ('name', 'facts', 'photo', 'street', 'google_link')
        