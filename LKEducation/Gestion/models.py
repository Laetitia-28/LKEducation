from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Classe(models.Model):
    code = models.CharField(max_length=5)
    libelle = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.libelle)
    
class Matiere(models.Model):
    intitule = models.CharField(max_length=50)

    def __str__(self):
        return str(self.intitule)

class Enseignant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = PhoneNumberField()
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, default='F')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class ClasseMatiere(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.PROTECT)
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    annee = models.IntegerField()

    def __str__(self):
        return f"{self.enseignant} {self.classe} {self.matiere}"
    
class Semestre(models.Model):
    numero = models.IntegerField
    pourcentage = models.FloatField
    def __str__ (self):
        return f"Semestre {self.numero}"
    
# class inscription(models.Model):


# class typeNote(models.Model):


# class note(models.Model):