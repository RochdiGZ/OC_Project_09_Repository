from django.shortcuts import render

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")  # HttpResponse("Accueil du site !")
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/signup.html", {"form": form})


def create_ticket(request):
    return render(request, "tickets/create_ticket.html")
