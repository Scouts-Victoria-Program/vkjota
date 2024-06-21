from django.urls import include, path

from . import views

app_name="vkjota"

urlpatterns=[
    path(
        "",
        views.HomePageView.as_view(),
        name="home",
    ),
    path(
        "old/",
        views.OldPageView.as_view(),
        name="old",
    ),
]
