from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("History", views.history, name="History"),
    path("Update5Min", views.Update5Min, name="Update5Min"),
    path("UpdateHour", views.UpdateHour, name="UpdateHour"),
    path("UpdateDay", views.UpdateDay, name="UpdateDay"),
    path("HistoryCreditRating", views.historyCreditRating, name="HistoryCreditRating")
]
