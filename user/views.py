from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)
