from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'8930498jsflkjsdk'})

def about(request):
    return render(request, 'generator/about.html', {'app':'Password Generator','version': '1.0.0'})

# Create your views here.
def eggs(request):
    return HttpResponse('I love eggs')

# Create your views here.
def password(request):

    characters = list('abcdefghijklmnopqrstuvzxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
