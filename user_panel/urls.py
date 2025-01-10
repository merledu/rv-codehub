from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = "user_panel"

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.custom_logout_view, name="mylogout"),
    path("login/", views.login_view, name="login_view")
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("logout1/", views.logout_view, name="logout1"),
]