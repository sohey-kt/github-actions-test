from django.urls import path
from app import views

urlpatterns = [
    path('app/', views.App_view),
]