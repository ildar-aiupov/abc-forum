from django.urls import path

from users import views


app_name = "users"

urlpatterns = [
    path(
        "logout/",
        views.MyLogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path(
        "login/",
        views.MyLoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path(
        "reset/<uidb64>/<token>/",
        views.MyPasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.MyPasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "password_reset/done/",
        views.MyPasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset/",
        views.MyPasswordResetView.as_view(
            template_name="users/password_reset_form.html"
        ),
        name="password_reset_form",
    ),
    path(
        "password_change/done/",
        views.MyPasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change/",
        views.MyPasswordChangeView.as_view(
            template_name="users/password_change_form.html"
        ),
        name="password_change",
    ),
]
