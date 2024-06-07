from django.urls import include, path

from . import views

app_name="vkjota"

urlpatterns=[
    path(
        "",
        views.HomePageView.as_view(),
        name="home",
    ),
]
