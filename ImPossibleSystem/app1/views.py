from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render (request,'home.html')

def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get("firstName")
        lname=request.POST.get("lastName")
        email=request.POST.get("email")
        pass1=request.POST.get('password1')
        pass2=request.POST.get('passsword2')

        print(uname,lname,email,pass1,pass2)
    return render (request, 'signup.html')

def LoginPage(request):
    return render (request, 'login.html')