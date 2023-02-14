from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View

from . import forms

from accounts.models import CustomUser
from .forms import UserRegistrationForm


class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields  # fields = ("username",)


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields  # fields = ("username",)


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # HttpResponse("Accueil du site !")
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/signup.html", {"form": form})


"""
def home(request):
    return HttpResponse("Accueil du site !")
"""
"""
def signup(request):
    context = {}
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # HttpResponse("Accueil du site !")
        else:
            context["errors"] = form.errors

    form = UserCreationForm()
    context["form"] = form
    return render(request, "accounts/signup.html", context=context)

"""
"""
def signup(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request, "accounts/signup.html", context={"error": "Les mots de passe ne correspondent pas"})
        CustomUser.objects.create_user(username=username, password=password1)
        return HttpResponse(f"Bienvenue {username} !")
    
    return render(request, "accounts/signup.html")
"""