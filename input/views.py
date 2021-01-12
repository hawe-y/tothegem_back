from django.shortcuts import render, redirect
from input.models import *

from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

class found_success(TemplateView):
    template_name = 'input/found_input_successpage.html'

class found_input(CreateView):
    model = Found_input
    template_name = 'input/found_input.html'
    fields = ['category', 'name', 'location', 'date', 'image', 'contact', 'description',]
    success_url = reverse_lazy('input:found_success')

    def form_valid(self, form):
        return super().form_valid(form)


class lost_success(TemplateView):
    template_name = 'input/lost_input_successpage.html'


class lost_input(CreateView):
    model = Lost_input
    template_name = 'input/lost_input.html'
    fields = ['category', 'name', 'location', 'date', 'money', 'image', 'contact', 'description',]
    success_url = reverse_lazy('input:found_success')

    def form_valid(self, form):
        return super().form_valid(form)