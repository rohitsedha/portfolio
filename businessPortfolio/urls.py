"""
URL configuration for businessPortfolio project.

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
from django.contrib import admin
from django.urls import path
from businessPortfolio import views  # Import views from the businessPortfolio app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about_view, name="home"),            # Root URL
    path('about/', views.about_view, name="about"),    # About URL
    path('contact/', views.contact_view, name="contact"),  # Contact URL
    path('index/', views.index_view, name="index"),    # Index URL
]
