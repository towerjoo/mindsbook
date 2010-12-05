# Create your views here.
from django.core.cache import cache
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def hello(request, template="hello.html"):
    return render_to_response(template, {}, context_instance=RequestContext(request))
