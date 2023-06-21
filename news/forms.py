from django import forms 
from .models import articles

class articlesCreationForm(forms.ModelForm):
    class Meta:
        model=articles
        fields=['title', 'desc','content','image', 'category']


class articlesUpdateForm(forms.ModelForm):
    class Meta:
        model=articles
        fields=['title', 'desc','content','image', 'category']