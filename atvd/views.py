from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Home')

def Diego(request):
    return render(request, 'Diego.html')

def Heloisa(request):
    return render(request, "Heloisa.html")
