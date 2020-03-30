"""onboarding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import path, include

from hellodoctor import views
from . import tmPartner

urlpatterns = [

    path('accounts/password_change/', PasswordChangeView.as_view(success_url='/download_csv/')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('download_csv/', views.download_doctors_data),
    path('upload_csv/', views.upload_csv),

    path('tmpartner/', tmPartner.tm_partner_form_request, name='tmPartner'),
    path('tmvolunteer/', tmPartner.tm_volunteer_form_request, name='tmvolunteer'),

    path('admin/', admin.site.urls),
]
