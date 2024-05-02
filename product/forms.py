from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Contact
        fields = '__all__'
