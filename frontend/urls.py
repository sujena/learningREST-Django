from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.searchBox, name='searchBox'),
    path('searchData/', views.searchData, name='searchData'),
    path('viewList/', views.viewList, name='viewList'),
    path('createData/', views.createData, name='createData'),
    path('updateData/', views.updateData, name='updateData'),
    path('deleteData/', views.deleteData, name='deleteData'),
]