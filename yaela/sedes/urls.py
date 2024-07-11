from django.urls import path
from . import views

urlpatterns = [
    path('', views.sede_list, name='sede_list'),
    path('new/', views.sede_create, name='sede_create'),
    path('<int:idsede>/edit/', views.sede_update, name='sede_update'),
    path('<int:idsede>/delete/', views.sede_delete, name='sede_delete'),
]
