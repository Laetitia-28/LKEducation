from .forms import LoginForm, SignupForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail


#LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user, backend = None)
                messages.add_message(request, messages.ERROR, 'Correct credentials.')
                return redirect('login')
            else:
                messages.add_message(request, messages.ERROR, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            # Authentication failed
            #return render(request, 'login.html', {'error': 'Invalid email or password.'})
            messages.add_message(request, messages.ERROR, 'Le formulaire est invalide. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



#LOGOUT VIEW
def logout_user(request):
    logout(request)
    return redirect('login')


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
            messages.add_message(request, messages.ERROR, 'Erreur.')
            for field, errors in form.errors.items():
            # Access the errors associated with each field
                for error in errors:
                    # Handle each error as needed
                    print(f"Error in field {field}: {error}")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


#CONTACT VIEW
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            # ENVOI DU MAIL
            # send_mail(
            #     request.POST['sujet'], #Objet du mail
            #     request.POST['message'], #message du mail
            #     request.POST['email'], #expéditeur du mail
            #     ['makenabgte@gmail.com'], #destinataire(s) du mail
            # )
            # FIN ENVOI MAIL


            form.save()
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

    return render(request, 'contact.html', {'form' : form})


#INDEX VIEW
def index(request):
    context = {}
    return render(request, "index.html", context)

def event(request):
    context = {}
    return render(request, 'event.html', context)

def appointment(request):
    context = {}
    return render(request, 'appointment.html', context)

def galerie(request):
    context = {}
    return render(request, 'galerie.html', context)

