from django.urls import path

from main import views


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "group/<int:group_id>/order_method/<slug:order_method>/",
        views.group_view,
        name="group_view",
    ),
    path("topic/<int:topic_id>/", views.topic_view, name="topic_view"),
    path("active_users/", views.active_users, name="active_users"),
    path("about_author/", views.about_author, name="about_author"),
    path("rules/", views.rules, name="rules"),
    path("today_posts/", views.today_posts, name="today_posts"),
    path("user_profile/<int:user_id>/", views.user_profile, name="user_profile"),
]
