from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
]