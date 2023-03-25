from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("post/<slug:slug>/", views.DetailPostView.as_view(), name="post_detail"),
    path("tag/<slug:tag>/", views.TagListView.as_view(), name="post_by_tag"),
]
