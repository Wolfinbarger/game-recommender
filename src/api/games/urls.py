from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("fake", views.fake_index, name="fake_index")
]