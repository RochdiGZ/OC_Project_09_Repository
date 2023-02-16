"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
import accounts.views
import flux.views
from django.conf import settings
from django.conf.urls.static import static

import subscriptions.views
import tickets.views
import reviews.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(
        template_name="accounts/login.html",
        redirect_authenticated_user=True),
         name="login"),
    path("logout/", accounts.views.logout_user, name="logout"),
    path("home/", flux.views.home, name="home"),
    path("signup/", accounts.views.signup, name="signup"),
    path("create-ticket/", tickets.views.create_ticket, name="create-ticket"),
    path("create-review/", reviews.views.create_review, name="create-review"),
    path("subscribers/", subscriptions.views.subscribers, name="subscribers"),
]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
