from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label = '', max_length = 256, widget=forms.TextInput(attrs={'placeholder': 'Search'}))