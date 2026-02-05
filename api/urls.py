from django.urls import path
from . import views

urlpatterns = [
    path("auth/token/", views.CustomTokenView.as_view()),
    path("auth/token/refresh/", views.CookieRefreshView.as_view()),
    path("me/", views.me_view),
    path("admin/panel/", views.admin_panel),
    path("premium-data/", views.premium_data)
]
