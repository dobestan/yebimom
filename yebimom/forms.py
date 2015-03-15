from django import forms

from django_summernote.widgets import SummernoteWidget


class ContactForm(forms.Form):
    title = forms.CharField(max_length = 255)
    content = forms.CharField(widget=SummernoteWidget())

    email = forms.EmailField()
