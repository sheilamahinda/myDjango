"""
URL configuration for SHEILZDJango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from SHEILZDJango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='my-index'),
    path('home/', views.full,name='my-blog-home'),
    path('post/', views.new,name='my-blog-post'),
    path('contact/', views.old,name='my-contact'),
    path('faq/', views.majina,name='my-faq'),
    path('about/', views.magari,name='my-about'),
    path('item/', views.copy,name='my-portfolio-item.'),
    path('overview/', views.paste,name='my-portfolio-overview'),
    path('pricing/', views.renew,name='my-pricing')
]
