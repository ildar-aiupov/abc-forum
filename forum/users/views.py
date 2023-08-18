from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)

from main.views import get_tree

from users.forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("main:index")
    template_name = "users/signup.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SignUp, self).get_context_data(*args, **kwargs)
        context["tree"] = get_tree(dontclear=True)
        return context


class MyLoginView(LoginView):
    def get_context_data(self, *args, **kwargs):
        context = super(MyLoginView, self).get_context_data(*args, **kwargs)
        context["tree"] = get_tree(dontclear=True)
        return context


class MyLogoutView(LogoutView):
    def get_context_data(self, *args, **kwargs):
        context = super(MyLogoutView, self).get_context_data(*args, **kwargs)
        context["tree"] = get_tree(dontclear=True)
        return context


class MyPasswordChangeView(PasswordChangeView):
    def get_context_data(self, *args, **kwargs):
        context = super(MyPasswordChangeView, self).get_context_data(*args, **kwargs)
        context["tree"] = get_tree(dontclear=True)
        return context


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    def get_context_data(self, *args, **kwargs):
        context = super(MyPasswordChangeDoneView, self).get_context_data(
            *args, **kwargs
        )
        context["tree"] = get_tree(dontclear=True)
        return context


class MyPasswordResetView(PasswordResetView):
    def get_context_data(self, *args, **kwargs):
        context = super(MyPasswordResetView, self).get_context_data(*args, **kwargs)
        context["tree"] = get_tree(dontclear=True)
        return context


class MyPasswordResetDoneView(PasswordResetDoneView):
    def get_context_data(self, *args, **kwargs):
        context = super(MyPasswordResetDoneView, self).get_context_data(*args, **kwargs)
        context["tree"] = get_tree(dontclear=True)
        return context


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    def get_context_data(self, *args, **kwargs):
        context = super(MyPasswordResetConfirmView, self).get_context_data(
            *args, **kwargs
        )
        context["tree"] = get_tree(dontclear=True)
        return context


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    def get_context_data(self, *args, **kwargs):
        context = super(MyPasswordResetCompleteView, self).get_context_data(
            *args, **kwargs
        )
        context["tree"] = get_tree(dontclear=True)
        return context
