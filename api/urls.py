from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path("auth/token/", views.CustomTokenView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
    path("me/", views.me_view),
    path("admin/panel/", views.admin_panel),
    path("premium-data/", views.premium_data)
]
