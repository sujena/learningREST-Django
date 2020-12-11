from api import views as api_views
from django.urls import path

urlpatterns = [
    path('',api_views.apiOverview, name="api-overview"),
    path('data-list/',api_views.dataList, name="data-list"),
    path('data-detail/<str:pk>/', api_views.dataDetail, name="data-detail"),
    path('data-create/',api_views.dataCreate, name="data-create"),
    path('data-update/<str:pk>/', api_views.dataUpdate, name="data-update"),
    path('data-delete/<str:pk>/', api_views.dataDelete, name="data-delete"),
]