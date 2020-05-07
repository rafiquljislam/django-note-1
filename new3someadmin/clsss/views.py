from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Test, TestForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class clsssview(FormView):
    template_name="clsss.html"
    form_class = TestForm
    success_url = 'clsss'

class show(TemplateView):
    template_name = 'clsss.html'
    model = Test
    