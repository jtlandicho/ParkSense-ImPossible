from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse

# Custom decorator to check for admin access
def is_admin(user):
    return user.is_superuser

def HomePage(request):
    return render(request, 'home.html')

def SignUpPage(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        # Check for existing username or email
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        # Create the user
        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')
    
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!")
            return redirect('login')

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required
def parking_slots(request):
    # Logic for parking slots
    return render(request, 'slots.html')

@login_required
@user_passes_test(is_admin)
def analytics(request):
    # Logic for analytics
    return render(request, 'analytics.html')
