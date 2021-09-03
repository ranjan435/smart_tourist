from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Place for recommendation', max_length=100)