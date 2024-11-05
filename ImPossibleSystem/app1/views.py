from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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
            return HttpResponse("Passwords do not match")
        
        # Create the user
        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()

        # Redirect to the login page after successful signup
        return redirect('login')  # Use the URL pattern name instead of the HTML file name
    
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required
def admin_view(request):
    if request.user.is_superuser or request.user.userprofile.is_admin:
        return render(request, 'admin_dashboard.html')
    else:
        return HttpResponseForbidden()

@login_required
def guest_view(request):
    if request.user.is_superuser or request.user.userprofile.is_admin:
        return redirect('admin_dashboard')  # Redirect admin to the admin view
    return render(request, 'guest_dashboard.html')