from django import forms

class SearchForm(forms.Form):
    '''
    A form used for accepting and processing searches.
    '''
    q = forms.CharField(label = '', max_length = 256, widget=forms.TextInput(attrs={'placeholder': 'Search'}))