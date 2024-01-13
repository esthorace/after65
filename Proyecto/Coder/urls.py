from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profesor/list", views.profesor_list, name="profesor_list"),
    path("profesor/form", views.profesor_form, name="profesor_form"),
]
