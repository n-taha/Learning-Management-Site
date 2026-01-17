from django.shortcuts import render , redirect
from django.contrib.auth import logout , login
from courses.forms import RegistrationForm , LoginForm
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class SignupView(FormView):
    template_name="courses/signup.html"
    form_class = RegistrationForm
    success_url  = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "courses/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.cleaned_data["user"]
        login(self.request, user)

        next_page = self.request.GET.get("next")
        if next_page:
            return redirect(next_page)

        return super().form_valid(form)


def signout(request ):
    logout(request)
    return redirect("home")

