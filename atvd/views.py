from django.shortcuts import render

# Create your views here.

def Diego(request):
    return render(request, 'Diego.html')

def Heloisa(request):
    return render(request, "Heloisa.html")
