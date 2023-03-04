from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.views.generic import View
from . import forms
from accounts.models import CustomUser


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


def signup(request):
    message1 = message2 = ""
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        try:
            test_user = CustomUser.objects.filter(username=username)
            if test_user:
                raise ValueError
            validate_password(password1)
            if password1 == password2:
                user = CustomUser.objects.filter(username=username)
                if not user.exists():
                    user = CustomUser.objects.create_user(username=username, password=password1)
                    login(request, user)
                    return redirect("home")
        except ValueError:
            message1 = "Le nom d'utilisateur existe déjà"
        except ValidationError:
            message2 = "Les mots de passe ne correspondent pas !"
        context = {'message1': message1, 'message2': message2}
        return render(request, "accounts/signup.html", context)
    else:
        return render(request, "accounts/signup.html")
