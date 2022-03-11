from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse('SHOP TEST')
def test(request):
    return HttpResponse('<h1>SHOP</h>')