from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. AKA request handler
def say_hello(request):
    x = 2
    y = 2
    return render(request, 'hello.html', { 'name': 'Juan'})
