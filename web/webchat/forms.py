from django import forms

class CommnetForm(forms.Form):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': '40', 'roes': '6'}))