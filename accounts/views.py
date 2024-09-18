from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as login_user,logout as logout_user
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        un=request.POST['username']
        pw=request.POST['password']
        user=authenticate(request,username=un,password=pw)
        if (user is not None):
            login_user(request,user)
            if user.is_superuser:
                
                return redirect("/admin")
            else:
                return redirect("/admin/commandes")
            
        else:
            messages.info(request,'Identifiant ou mot de passe incorrect')
    
    return render(request,'login.html')

def logout(request):
    logout_user(request)
    return redirect('/accounts/login/')

def register(request):
    if request.method == 'POST':
        un=request.POST['username']
        pw=request.POST['password']
        cpw=request.POST['confirmpassword']
        em=request.POST['email']
        if len(pw)< 8:
            messages.error(request,'Le mot de passe est trop court (au moins 8 caractères)')
        elif cpw != pw:
            messages.error(request,'Vérifiez encore le mot de passe')
        else:
            user=User.objects.create_user(email=em,username=un)
            user.set_password(raw_password=pw)
            user.save()
            return redirect('/accounts/login/')
    return render(request,'register.html')


