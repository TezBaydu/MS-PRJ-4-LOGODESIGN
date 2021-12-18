from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_packages, name='projects_packages'),
    path('<package_id>', views.package_detail, name='package_detail'),
]
