from django.urls import path, include
from .views import authView
#from core import views

app_name = "base"

urlpatterns = [
        path("register/", authView, name="register"),
        path("accounts/", include("django.contrib.auth.urls"),)
]
