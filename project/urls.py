"""project URL Configuration

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
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import login, views as authviews
from users import views as user_view
from django.conf import Settings, settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_view.register,name='register'),
    path('profile/',user_view.profile,name='profile'),
    path('login/',authviews.LoginView.as_view(template_name='users\login.html'),name='login'),
    path('logout/',authviews.LogoutView.as_view(template_name='users\logout.html'),name='logout'),

    path(
        'password-reset/',
        authviews.PasswordResetView.as_view(template_name='users\password_reset.html'),
        name='password_reset'),    
        
    path(
        'password-reset/done/',
        authviews.PasswordResetDoneView.as_view(template_name='users\password_reset_done.html'),
        name='password_reset_done'),

    path(
        'password-reset-confirm/<uidb64>/<token>/',
        authviews.PasswordResetConfirmView.as_view(template_name='users\password_reset_confirm.html'),
        name='password_reset_confirm'),

   path(
        'password-reset-complete/',
        authviews.PasswordResetCompleteView.as_view(template_name='users\password_reset_complete.html'),
        name='password_reset_complete'),    
    
    path('',include('blog.url')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
