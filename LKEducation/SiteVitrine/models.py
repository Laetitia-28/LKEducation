from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
    
class galerie(models.Model):
    titre = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='location') #Mettre le dossier du quel les images seront importées

    def __str__(self):
        return str(self.titre)


#CLASSE ARTICLE
class article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    image = models.ImageField(upload_to='location') #Mettre le dossier du quel les images seront importées
    datePublication = models.DateTimeField(auto_now_add=True) #la date de publication s'enregistrera de manière automatique à l'enregistrement

    def __str__(self):
        return str(self.titre) #Retourne le titre de l'article


#CLASSE EVENEMENT
class evenement(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    lieu = models.CharField(max_length=20)
    image = models.ImageField(upload_to='location') #Mettre le dossier dans lequel les images seront importées
    date = models.DateTimeField()

    def __str__(self):
        return str(self.titre) #Retourne le titre de l'évènement


#CLASSE USER
class UserManager(BaseUserManager): # Pour les paramètres de connexion
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse mail')
        user = self.model(email=self.normalize_email(email), )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(email, password=password, )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password, )
        user.is_staff = True
        user.admin = True
        user.save(using=self._db)
        return user  

class User(AbstractBaseUser):
    nom = models.CharField(max_length=50, default="")
    prenom = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True)
    contact = PhoneNumberField()
    nationalité = models.CharField(max_length=50, default="")
    date_naissance = models.DateField(default=datetime.date.today)
    lieu = models.CharField(max_length=50, default="")
    sexe = models.CharField(max_length=1, default="F")
    photo = models.ImageField(upload_to='location', blank=False, null=True)
    dernier_diplome = models.CharField(max_length=100, default="")
    moyenne_et_annee = models.CharField(max_length=50, default="")
    Etudes_en_cours = models.CharField(max_length=150, default="")
    Domaine_etudes_en_France = models.CharField(max_length=100, default="")
    commentaire = models.TextField(blank=True)
    #message = models.TextField(blank=True) #Blank messages will concern the signup page and those not blank concern the contact page
    created_at = models.DateTimeField(auto_now_add=True) #date création utilisateur automatique
    updated_at = models.DateTimeField(auto_now=True) # date modification automatique également
    admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.email

    USERNAME_FIELD = 'email' # Les utilisateurs vont se connecter avec leurs adresses mail
    REQUIRED_FIELDS = []

    objects = UserManager() # les utilisateurs sont les intances de classe de UserManager()

    def get_full_name(self):
        # Combiner le nom et le prénom pour obtenir le nom complet
        return f"{self.nom} {self.prenom}"

    def set_password(self, raw_password):
       self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def is_admin(self):
        """L'utilisateur est-il un membre administrateur?"""
        return self.admin

    def has_perm(self,perm,obj=None):
        """L'utilisateur a-t-il une autorisation spécifique ?"""
        """Réponse la plus simple possible : Oui, toujours"""
        return True

    def has_module_perms(self, app_label):
        # "L'utilisateur dispose-t-il des autorisations nécessaires pour voir l'application ?`app_label`?"
        # Réponse la plus simple possible : Oui, toujours
        return True


#CLASSE CONTACT
class Contact(models.Model):
    nom_et_prenom = models.CharField(max_length=50, default="")
    email = models.EmailField()
    contact = PhoneNumberField()
    sujet = models.CharField(max_length=50, default="")
    message = models.TextField(blank=False) #Blank messages will concern the signup page and those not blank concern the contact page
    est_repondu = models.BooleanField(default=False)

#CLASSE MODELE RENDEZ-VOUS
class modele_rdv(models.Model):
    DateDebut = models.DateTimeField()
    DateFin = models.DateTimeField()
    disponible = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT) #clé étrangère utilisateur ayant crée le rendez-vous
    
    def __str__(self):
        return f"{self.user} {self.DateDebut} {self.disponible}"

#CLASSE RENDEZ VOUS
class rendezvous(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    rdv = models.ForeignKey(modele_rdv, on_delete=models.PROTECT)

#CLASSE NOTIFICATION
class notification(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT) #clé étrangère matérialisant le destinataire du message

#CLASSE DOCUMENT
class document(models.Model):
    intitule = models.CharField(max_length=20, default=" ")
    document = models.FileField(upload_to="location", default=" ") # Mettre le dossier dans lequel les documents seront importées
    taille = models.IntegerField() # la taille des documents ne doit pas excéder 5Mo
    user = models.ForeignKey(User, on_delete=models.PROTECT)

#CLASSE HISTORIQUE DE PAIE
class historique_paie(models.Model):
    montant = models.FloatField()
    nature = models.CharField(max_length=10) # Il peut s'agir d'un paiement cash ou en ligne
    date = models.DateTimeField() #date à laquelle la transaction a été effectuée
    user = models.ForeignKey(User, on_delete=models.PROTECT) #user client ayant effectué la transaction