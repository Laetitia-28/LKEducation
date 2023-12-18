from django import forms
from SiteVitrine.models import User, Contact

class ClientForm(forms.ModelForm):
    class Meta:
        sexe = forms.ChoiceField(choices=[('M', 'M'), ('F', 'F')], widget=forms.Select)
        model = User
        fields = ['nom', 'prenom', 'email', 'contact', 'date_naissance', 'sexe']  # Inclure les champs souhaités pour l'inscription
        widgets = {             
            'date_naissance': forms.DateInput(attrs={'type': 'date'})
        }
    
    # error_messages = {
    #     'email': {
    #         'unique': "Cette adresse e-mail est déjà utilisée.",
    #     },
    #     'contact': {
    #         'invalid': "Le format du numéro de téléphone est incorrect.",
    #     },
    # }

    # Exclure le champ de mot de passe de l'affichage
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        # self.fields['password'].widget = forms.HiddenInput()
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class ModifierUtilisateurForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'contact', 'date_naissance', 'sexe', 'commentaire']
        widgets = {             
            'date_naissance': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(ModifierUtilisateurForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class MailReponseForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["email", "sujet", "message" ]
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})