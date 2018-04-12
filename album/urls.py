"""myapps2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from album import views


urlpatterns = [
    path('',views.first_view,name='base'),
    path('category/',views.category,name='category-list'),
    path('category/<int:category_id>/detail/', views.category_detail, name='category-detail'),
    
    path('photo/', views.PhotoListView.as_view(), name='photo-list'),
    path('photo/<int:pk>/detail/', views.PhotoDetailView.as_view(), name='photo-detail'),
    # Update foto
    path('photo/<int:pk>/update/', views.PhotoUpdate.as_view(), name='photo-update'),
    #Create foto
    path('photo/create/', views.PhotoCreate.as_view(), name='photo-create'),
    #Delete foto
    path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo-delete'),
     # Update category
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category-update'),
    #Create category
    path('category/create/', views.CategoryCreate.as_view(), name='category-create'),
    #Delete category
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
]
