# forms.py
from django import forms
from .models import News


class SearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by title…'
        })
    )


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # exclude auto fields; include what a user should edit
        fields = ['title', 'content', 'photo', 'category', 'bool']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'bool': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
