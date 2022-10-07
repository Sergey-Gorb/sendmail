# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Содержание', widget=forms.Textarea, required=True)