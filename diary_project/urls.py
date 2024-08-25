"""
URL configuration for diary_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from diary import views
from django.contrib.auth import views as auth_views
urlpatterns = [
     path('accounts/', include('django.contrib.auth.urls')),

    path('', views.entry_list, name='entry-list'),
    path('entry/create/', views.entry_create, name='entry-create'),
    path('entry/<int:pk>/update/', views.entry_update, name='entry-update'),
    path('entry/<int:pk>/delete/', views.entry_delete, name='entry-delete'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
