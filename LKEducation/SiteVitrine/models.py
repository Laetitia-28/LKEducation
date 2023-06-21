from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
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
        User = self.model(email=self.normalize_email(email), )
        User.set_password(password)
        User.save(using=self._db)
        return User

    # def create_studentuser(self, email, password):
    #     User = self.create_user(email, password=password, )
    #     User.etudiant = True
    #     User.save(using=self._db)
    #     return User
    
    # def create_clientuser(self, email, password):
    #     User = self.create_user(email, password=password, )
    #     User.etudiant = True
    #     User.client = True
    #     User.save(using=self._db)
    #     return User

    def create_staffuser(self, email, password):
        User = self.create_user(email, password=password, )
        User.staff = True
        User.save(using=self._db)
        return User

    def create_superuser(self, email, password):
        User = self.create_user(email, password=password, )
        User.staff = True
        User.admin = True
        User.save(using=self._db)
        return User
    

class user(AbstractBaseUser):
    nom = models.CharField(max_length=50, default="")
    prenom = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True)
    contact = PhoneNumberField()
    date_naissance = models.DateField(default=datetime.date.today)
    sexe = models.CharField(max_length=1, default="F")
    password = models.CharField (max_length=10)
    photo = models.ImageField(upload_to='location', blank=False, null=True)
    message = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True) #date création utilisateur automatique
    updated_at = models.DateTimeField(auto_now=True) # date modification automatique également
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def _str_(self):
        return self.email

    USERNAME_FIELD = 'email' # Les utilisateurs vont se connecter avec leurs adresses mail
    REQUIRED_FIELDS = []

    objects = UserManager() # les utilisateurs sont les intances de classe de UserManager()

    def has_perm(self,perm,obj=None):
        """L'utilisateur a-t-il une autorisation spécifique ?"""
        """Réponse la plus simple possible : Oui, toujours"""
        return True

    def has_module_perms(self, app_label):
        # "L'utilisateur dispose-t-il des autorisations nécessaires pour voir l'application ?`app_label`?"
        # Réponse la plus simple possible : Oui, toujours
        return True


#CLASSE MODELE RENDEZ-VOUS
class modele_rdv(models.Model):
    DateDebut = models.DateTimeField()
    DateFin = models.DateTimeField()
    disponible = models.BooleanField(default=True)
    user = models.ForeignKey(user, on_delete=models.PROTECT) #clé étrangère utilisateur ayant crée le rendez-vous
    
    def __str__(self):
        return f"{self.user} {self.DateDebut} {self.disponible}"

#CLASSE RENDEZ VOUS
class rendezvous(models.Model):
    user = models.ForeignKey(user, on_delete=models.PROTECT)
    rdv = models.ForeignKey(modele_rdv, on_delete=models.PROTECT)

#CLASSE NOTIFICATION
class notification(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user, on_delete=models.PROTECT) #clé étrangère matérialisant le destinataire du message

#CLASSE DOCUMENT
class document(models.Model):
    intitule = models.CharField(max_length=20, default=" ")
    document = models.FileField(upload_to="location", default=" ") # Mettre le dossier dans lequel les documents seront importées
    taille = models.IntegerField() # la taille des documents ne doit pas excéder 5Mo
    user = models.ForeignKey(user, on_delete=models.PROTECT)

#CLASSE HISTORIQUE DE PAIE
class historique_paie(models.Model):
    montant = models.FloatField()
    nature = models.CharField(max_length=10) # Il peut s'agir d'un paiement cash ou en ligne
    date = models.DateTimeField() #date à laquelle la transaction a été effectuée
    user = models.ForeignKey(user, on_delete=models.PROTECT) #user client ayant effectué la transaction