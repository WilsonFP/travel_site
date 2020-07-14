from django import forms
from .models import Search

class SearchForm(forms.ModelForm):
    destination = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Destination"}))
    class Meta:
        model = Search
        fields = [
            'destination'
        ]
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "item" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     else:
    #         return title
