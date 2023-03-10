"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.feed, name='feed')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='feed')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(
        template_name="accounts/login.html",
        redirect_authenticated_user=True),
         name="login"),
    path("logout/", accounts.views.logout_user, name="logout"),
    path("signup/", include("accounts.urls")),
    path("feed/", include("feeds.urls")),
    path("posts/", include("posts.urls")),
    path("reviews/", include("reviews.urls")),
    path("subscribers/", include("subscriptions.urls")),
    path("tickets/", include("tickets.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
