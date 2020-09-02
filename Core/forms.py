from django.forms import Form
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(Form):
    from_email = forms.EmailField(required=True, label=_("email"))
    subject = forms.CharField(required=True, label=_("subject"))
    message = forms.CharField(widget=forms.Textarea, required=True, label=_("message"))
