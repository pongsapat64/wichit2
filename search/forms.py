# forms.py
from django import forms

from search.models import wicha

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, )


class WichaForm(forms.ModelForm):
    class Meta:
        model = wicha
        fields = ['subject_id','name']