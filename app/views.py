from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html", {})
