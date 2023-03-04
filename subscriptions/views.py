from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import CustomUser
from subscriptions.models import UserFollows


@login_required
def subscribers(request):
    user = get_user(request)
    message = ''
    if request.method == "POST":
        # Cas où l'utilisateur souhaite suivre quelqu'un
        if 'sub' in request.POST:
            name = request.POST.get('name')
            if name in [user.username for user in CustomUser.objects.all()] \
                    and name != user.username \
                    and name not in [pair.followed_user.username for pair in UserFollows.objects.filter(user=user)]:
                pair = UserFollows(
                    user=user,
                    followed_user=CustomUser.objects.get(username=name)
                )
                pair.full_clean()
                pair.save()
            else:
                message = "Le nom rentré n'a pas été trouvé, veuillez recommencer."
        # Cas où l'utilisateur souhaite arrêter de suivre une personne
        elif 'unsub' in request.POST:
            unsub_name = request.POST.get('unsub')
            unsub_user = CustomUser.objects.get(username=unsub_name)
            unsub_pair = UserFollows.objects.get(user=user, followed_user=unsub_user)
            unsub_pair.delete()
    followed_users = UserFollows.objects.filter(user=user)
    followed_bys = UserFollows.objects.filter(followed_user=user)
    context = {
        "followed_users": followed_users,
        "followed_bys": followed_bys,
        "user": user,
        'message': message
    }
    return render(request, 'subscriptions/subscribers.html', context)
