from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Car_mark, Car_model, Car_engin_type
from pprint import pprint
# Create your views here.


class MarkList(ListView):
    model = Car_mark
    ordering = 'name'
    template_name = 'index.html'
    context_object_name = 'marka'


class ModelList(ListView):
    model = Car_model
    ordering = 'name'
    template_name = 'index.html'
    context_object_name = 'model'




