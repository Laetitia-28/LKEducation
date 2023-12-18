from django.core.exceptions import ValidationError
import re


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'
    

class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir au moins un chiffre.', code='password_no_numbers'
            )
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'
    

class ContainsSpecialCaracterValidator:
    def validate(self, password, user=None):
        if not re.search(r'[!@#$%^&*()_+=\[\]{};:"\|,.<>?`~]', password):
            raise ValidationError(
                'Le mot de passe doit contenir au moins un caractère spécial (@, %, £, etc.).',
                code='password_no_special_characters'
            )
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un caractère spécial.'