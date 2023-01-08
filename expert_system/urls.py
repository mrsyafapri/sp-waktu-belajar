from django.contrib import admin
from django.urls import path

from .views import HomeView, FormView, AboutView, ResultView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("form/", FormView.as_view(), name="form"),
    path("result/", ResultView.as_view(), name="result"),
    path("about/", AboutView.as_view(), name="about"),
]
