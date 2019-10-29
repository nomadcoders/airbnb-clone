from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("sigup", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
]
