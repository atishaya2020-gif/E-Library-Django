from django import forms
from .models import EBook


class EBooksForm(forms.ModelForm):

    class Meta:

        model = EBook

        fields = [
            'title',
            'summary',
            'pages',
            'pdf',
            'category',
        ]