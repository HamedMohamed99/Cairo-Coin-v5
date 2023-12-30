from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("history", views.history, name="history"),
    path("Update5Min", views.Update5Min, name="Update5Min"),
    path("UpdateHour", views.UpdateHour, name="UpdateHour"),
    path("UpdateDay", views.UpdateDay, name="UpdateDay"),
    path("historycreditrating", views.historyCreditRating, name="historycreditrating"),
    path("calculator", views.Calculator, name="calculator")
]
