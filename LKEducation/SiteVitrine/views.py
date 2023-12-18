from .forms import LoginForm, SignupForm, ContactForm, MyPasswordResetForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string

#LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # Authentification réussie : stocker l'identifiant de l'utilisateur dans la session
                login(request, user, backend = None)
                #messages.add_message(request, messages.ERROR, 'Correct credentials.')

                # # Stocker le nom et la photo de l'utilisateur dans la session
                # request.session['user_name'] = user.get_full_name()
                # request.session['user_photo'] = user.photo.url if user.photo else None

                # Redirection vers une page du dashboard
                return redirect('Gestion:liste_clients')
            else:
                messages.add_message(request, messages.ERROR, 'Nom d\'utilisateur ou mot de passe incorrect!')
                for field, errors in form.errors.items():
                # Access the errors associated with each field
                    for error in errors:
                        # Handle each error as needed
                        print(f"Error in field {field}: {error}")

                form = LoginForm()
        else:
            messages.add_message(request, messages.ERROR, 'Le formulaire est invalide. Veuillez corriger les erreurs ci-dessous.')
            for field, errors in form.errors.items():
            # Access the errors associated with each field
                for error in errors:
                    # Handle each error as needed
                    print(f"Error in field {field}: {error}")
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


#SIGNUP VIEW
def signup(request):    
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.add_message(request, messages.ERROR, 'Formulaire sauvegardé avec succès.')
            # You can perform additional operations here, such as sending a confirmation email
            return redirect('login')  # Replace 'login' with the URL name for your login page
        else:
            #messages.add_message(request, messages.ERROR, 'Erreur.')
            for field, errors in form.errors.items():
            # Access the errors associated with each field
                for error in errors:
                    # Handle each error as needed
                    print(f"Error in field {field}: {error}")
            
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


#CONTACT VIEW
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #ENVOI DU MAIL

            message_html = render_to_string('Contact/email_template.html', {
                'nom_et_prenom': request.POST['nom_et_prenom'],
                'email': request.POST['email'],
                'contact': request.POST['contact'],
                'sujet': request.POST['sujet'],
                'message': request.POST['message'],
            })
            
            send_mail(
                'Nouvelle Inscription', #Objet du mail
                '', #message du mail
                request.POST['email'], #expéditeur du mail
                ['makenabgte@gmail.com'], #destinataire(s) du mail
                html_message=message_html,
            )
            #FIN ENVOI MAIL

            form.save()
            print(request.POST['email'])
            messages.add_message(request, messages.ERROR, 'Message envoyé.')

            return redirect('contact')
        else:
            messages.add_message(request, messages.ERROR, 'Erreur lors de l\'envoi du message.')
            for field, errors in form.errors.items():
            # Access the errors associated with each field
                for error in errors:
                    # Handle each error as needed
                    print(f"Error in field {field}: {error}")
    else:
        form = ContactForm()

    return render(request, 'Contact/contact.html', {'form' : form})


#INDEX VIEW
def index(request):
    context = {}
    return render(request, "index.html", context)

#EVENTS VIEW (Actualités)
def event(request):
    context = {}
    return render(request, 'event.html', context)

#APPOINTMENT VIEW
def appointment(request):
    context = {}
    return render(request, 'appointment.html', context)

#GALLERY VIEW
def galerie(request):
    context = {}
    return render(request, 'galerie.html', context)

#SERVICES VIEW
def services(request):
    context = {}
    return render(request, 'services.html', context)

#PARTNERS VIEWS

def partenaires_allemagne(request):
    context = {}
    return render(request, 'Partenaires/partenaires_allemagne.html', context)

def partenaires_espagne(request):
    context = {}
    return render(request, 'Partenaires/partenaires_espagne.html', context)

def partenaires_lituanie(request):
    context = {}
    return render(request, 'Partenaires/partenaires_lituanie.html', context)

def partenaires_france(request):
    context = {}
    return render(request, 'Partenaires/partenaires_france.html', context)

# REINITIALISATION DE MOT DE PASSE
def password_reset_form(request):
    if request.method == 'POST':
        form = MyPasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_reset_Done')
    else:
        form = PasswordResetForm()
    
    return render(request, 'password_reset/form.html', {'form': form})

def password_reset_done(request):
    return render(request, 'password_reset/done.html')

def password_reset_confirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                # Hacher le nouveau mot de passe réinitialisé avec la méthode make_password
                new_password = form.cleaned_data['new_password1']
                hashed_password = make_password(new_password)

                # Enregistrez le mot de passe haché dans le modèle utilisateur
                user.password = hashed_password

                # Enregistrez l'utilisateur mis à jour dans la base de données
                user.save()
                form.save()
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
    else:
        # Gérer le cas où le lien de réinitialisation est invalide ou a expiré
        form = None
    
    context = {
        'uidb64': uidb64,
        'token': token,
        'form': form,
    }

    return render(request, 'password_reset/confirm.html', context)

def password_reset_complete(request):
    return render(request, 'password_reset/complete.html')