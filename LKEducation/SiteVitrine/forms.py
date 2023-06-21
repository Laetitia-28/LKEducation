from django import forms
from django.forms import ModelForm
from .models import UserManager, user
from phonenumber_field.formfields import PhoneNumberField


class SignupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    contact = PhoneNumberField(widget=forms.TextInput())
    class Meta:
        model = user
        fields = ["nom", "prenom", "email", "contact", "date_naissance", "password", "photo"]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'my-form'})

class ContactForm(ModelForm):
    contact = PhoneNumberField(widget=forms.TextInput())
    class Meta:
        model = user
        fields = ["nom", "prenom", "email", "contact", "message", ]
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'my-form'})