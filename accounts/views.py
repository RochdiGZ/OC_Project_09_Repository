from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View

from . import forms

from accounts.models import CustomUser
from .forms import SignupForm


# https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP
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


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields  # fields = ("username",)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")  # HttpResponse("Accueil du site !")
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})
