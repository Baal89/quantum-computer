from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
    
@login_required
def logout(request):
    """
    A view that logs the user out and redirects back to the index page.
    With the login_required decorators we prevent possible critical failure of the system,
    preventing the access of this page only for the user already logged in.
    """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    """
    A view that manages the login form.
    The firs if statement prevent the access of the login page after the 
    user is logged in.
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username_or_email'],
                                    password=request.POST['password'])
                                    
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
    
def registration(request):
    """
    A view that manages the registration form
    The firs if statement prevent the access of the registration page after the 
    user is registered.
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
    
@login_required
def profile(request):
    """
    A view that displays the profile page of a logged in user.
    With the login_required decorators we prevent possible critical failure of the system,
    preventing the access of this page only for the user already logged in.
    """
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
