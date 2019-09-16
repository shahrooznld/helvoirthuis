from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View
from .models import Family


# Create your views here.


class HomeView(View):
    def get(self, request):
        name = Family.objects.all()
        return render_to_response('x.html', {'family': name}, RequestContext(request))


class XView(View):
    def get(self, request):
        famil = Family.objects.all()
        return render_to_response('index.html', {'family': famil}, RequestContext(request))
