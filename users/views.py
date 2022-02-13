from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import User

# Create your views here.

def home(request):
    return render(request, 'user/home.html')


def register(request):
    form = UserForm()
    if request.method == "POST":
        #request.POST formdaki normal fieldlerim için request.FİLES profile picture vs gibi filelerim için
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():#validation kurallarına uyuyormu bakıor.(karakter sayısı falan)
            form.save()
            username = form.cleaned_data["username"] #formdan username yibu methodla cektik ve usernameye atatdım
            password = form.cleaned_data["password1"]#formdan passwordu bu methodla cektik ve password atatdım
            # veya
            # username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=password)#authenticate ettik ve böylebiruser varsa usere atadım
            login(request, user)#django login methodu ile useri login ettim
            return redirect("home") #sonra home git dedim
    context = {
        "form_user" : form
    }
    return render(request, "user/register.html", context)

def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return redirect('home')    

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():#validation kurallarına uyuyormu bakıor(karakter sayısı falan)
        user = form.get_user() #AuthenticationFormun methotlarından get_user ile formdaki useri usere atadık 
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('home')
    return render(request, 'user/login.html', {"form": form})

def newpost(request):
    return render(request, 'user/newpost.html')


def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request, id):
    user = User.objects.get(id=id)
    form = ProfileForm(instance=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Your profile has been updated!!")
            form.save()
            return redirect("home")
    context= {
        "form":form
    }
    return render(request, "user/profile.html", context)