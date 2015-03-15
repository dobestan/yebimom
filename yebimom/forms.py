from django import forms

from django_summernote.widgets import SummernoteWidget


class ContactForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=SummernoteWidget())
    phone = forms.CharField(max_length=16)

    email = forms.EmailField()
