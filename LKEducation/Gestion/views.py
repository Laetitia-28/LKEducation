from django.shortcuts import render, redirect, get_object_or_404
from SiteVitrine.models import User, Contact
from .forms import ClientForm, ModifierUtilisateurForm, MailReponseForm
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.core.mail import send_mail

#Restreindre l'accès de cette partie du site aux utilisateurs connectés

# Index view
@login_required
def index(request):
    context = {}
    return render(request, "index.html", context)

#Vérifier si l'utilisateur en session est un administrateur afin de n'accorder les actions d'ajout, modification et suppression à lui seul
def is_admin(user):
    return user.is_admin()


# Vue pour la liste des utilisateurs 
@login_required
def liste_utilisateurs(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'utilisateurs.html', context)


# Ajouter un client
@user_passes_test(is_admin, login_url=reverse_lazy('Gestion:liste_clients'))
def Ajouter_Client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # Créer un nouvel utilisateur sans mot de passe
            new_user = form.save()
            new_user.set_password(get_random_string(10))  # Génération d'un mot de passe aléatoire
            # new_user.admin = False  # Définir le rôle de l'utilisateur comme non administrateur (client)
            # new_user.is_staff = False
            new_user.save()
            messages.add_message(request, messages.ERROR, 'Ajout succesful.')
            return redirect('Gestion:liste_clients')  # Rediriger vers la vue de gestion des clients après l'inscription réussie
        else:
            messages.add_message(request, messages.ERROR, 'Erreur.')
            for field, errors in form.errors.items():
            # Access the errors associated with each field
                for error in errors:
                    # Handle each error as needed
                    print(f"Error in field {field}: {error}")
    else:
        form = ClientForm()
    
    context = {
        'form': form,
    }
    return render(request, 'ajout_client.html', context)


# Modifier les informations d'un client
@user_passes_test(is_admin, login_url=reverse_lazy('Gestion:liste_clients'))
def modifier_client(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = ModifierUtilisateurForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informations utilisateur mises à jour avec succès.')
            return redirect('Gestion:liste_clients')
        else:
            #print(form.errors)
            messages.add_message(request, messages.ERROR, 'Erreur.')
            for field, errors in form.errors.items():
            # Access the errors associated with each field
                for error in errors:
                    # Handle each error as needed
                    print(f"Error in field {field}: {error}")
    else:
        form = ModifierUtilisateurForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'modifier_client.html', context)

# Supprimer un client
@user_passes_test(is_admin, login_url=reverse_lazy('Gestion:liste_clients'))
def supprimer_client(request, user_id):
    # Récupérer le client à supprimer
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        # Supprimer le client
        user.delete()
        return redirect('Gestion:liste_clients')

    return render(request, 'supprimer_client.html', {'user': user})


# Vue pour la liste des contacts (messages laissés sur le site via la page contact)
@login_required
def liste_contact(request):
    contacts = Contact.objects.all()
    context = {'contacts' : contacts}
    return render(request, 'contacts.html', context)

# Répondre à un message par mail
@user_passes_test(is_admin, login_url=reverse_lazy('Gestion:liste_contacts'))
def repondre_message(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = MailReponseForm(request.POST)
        if form.is_valid():
            #ENVOI DU MAIL
            send_mail(
                f"Re: {contact.sujet}", #Objet du mail
                request.POST['message'], #message du mail
                'makenabgte@gmail.com', #expéditeur du mail
                [contact.email], #destinataire(s) du mail
            )
            #FIN ENVOI MAIL

            # Marquer le message comme répondu dans la BD
            contact.est_repondu = True
            contact.save()

            return redirect('Gestion:liste_contacts')
        else:
            for field, errors in form.errors.items():
            # Access the errors associated with each field
                for error in errors:
                    # Handle each error as needed
                    print(f"Error in field {field}: {error}")
    else:
        form = MailReponseForm(initial={'email': contact.email, 'sujet': contact.sujet})

    context = {
        'form': form,
        'contact': contact,
    }
    return render(request, 'repondre_message.html', context)

# Supprimer un message 
@user_passes_test(is_admin, login_url=reverse_lazy('Gestion:liste_contacts'))
def supprimer_message(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        # Supprimer le client
        contact.delete()
        return redirect('Gestion:liste_contacts')

    return render(request, 'supprimer_message.html', {'contact': contact})


# Vue pour l'ensemble des candidatures en cours
@login_required
def candidatures(request):
    context = {}
    return render(request, "candidatures.html", context)


# Vue pour les notifications
@login_required
def discussion(request):
    context = {}
    return render(request, "discussion.html", context)

# Vue pour le profile 
@login_required
def profile(request):
    context = {}
    return render(request, "profile.html", context)

# Vue pour l'ensemble des rendez-vous
@login_required
def rendez_vous(request):
    context = {}
    return render(request, "rendez_vous.html", context)

#LOGOUT VIEW
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')
