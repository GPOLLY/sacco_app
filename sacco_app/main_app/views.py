from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse


# home page
def home_view (request):
	return render(request,'site_app/index.html',locals())