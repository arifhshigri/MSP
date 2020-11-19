from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="/login/")
def profile(request):
    context={}
    context['segment'] ='profile'
    html_template = loader.get_template('profile.html')
    return HttpResponse(html_template.render(context,request))
