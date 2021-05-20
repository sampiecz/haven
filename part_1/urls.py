from django.urls import path
from . import views

urlpatterns = [
    path("<str:propertyId>", views.index, name="index"),
    path("<str:propertyId>/<str:endpoint_pk>", views.index_v2, name="index_v2"),
]
