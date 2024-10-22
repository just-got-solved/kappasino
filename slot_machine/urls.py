from django.urls import path
from . import views

urlpatterns = [
    path('', views.slot_machine_view, name='slot_machine'),
]
