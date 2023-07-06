from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *
from phonenumber_field.formfields import PhoneNumberField


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'my-form'})


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("nom", "prenom", "email", "contact", "date_naissance", "password1", "password2", "photo")
        widgets = {             
            'date_naissance': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'my-form'})
     
#     def save(self):
#         user = super().save(commit=False)
#         user.admin=False
#         user.set_password(self.cleaned_data['password'])
#         user.save()       
#         return user

class ContactForm(ModelForm):
    contact = PhoneNumberField(widget=forms.TextInput())
    class Meta:
        model = Contact
        fields = ["nom_et_prenom", "email", "contact", "sujet", "message" ]
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'my-form'})