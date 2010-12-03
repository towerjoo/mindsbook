# Create your views here.
from django.core.cache import cache
from django.views.generic.simple import direct_to_template
from guestbook.forms import CreateGreetingForm
from guestbook.models import Greeting
from django.http import HttpRsponse

def hello(request):
    return HttpRsponse("hello world")
