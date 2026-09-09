from django.urls import path
from . import views

urlpatterns = [
    # ✕ 修正前: path("", views.index, name="index"),
    path("", views.recommend_view, name="recommend_view"),
    path("api/recommend/", views.recommend_view, name="recommend_api"),
]