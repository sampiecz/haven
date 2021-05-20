from django.urls import path
from . import views

urlpatterns = [
    path("<str:propertyId>", views.index, name="index"),
]
