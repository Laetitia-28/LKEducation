from .forms import LoginForm, SignupForm, ContactForm
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('Gestion:index') #Replace 'dashboard' with the url name for your dashboard page
        
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form' : form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # You can perform additional operations here, such as sending a confirmation email
            form.save()
            return redirect('login')  # Replace 'login' with the URL name for your login page
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form' : form})


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

