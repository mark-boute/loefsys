from django.urls import path, include

from users.views import ProfileDetailView

app_name = "users"

urlpatterns = [
    path(
        "members/",
        include(
            [
                path("profile/", ProfileDetailView.as_view(), name="profile"),
                path("profile/<int:pk>", ProfileDetailView.as_view(), name="profile"),
            ]
        ),
    ),
]
