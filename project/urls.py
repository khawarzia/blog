"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from loginreg import views as loginview
from posting import views as postview

urlpatterns = [
    path('admin/', admin.site.urls),

    # loginref urls

    path('',loginview.home,name='home'),
    path('login',loginview.login,name='login'),
    path('logout',loginview.logout,name='logout'),
    path('signup',loginview.signup,name='signup'),


    # posting urls

    path('profile/<str:usr>',postview.profilepage,name='profile'),
    path('new-post',postview.newpost,name='new-post'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)