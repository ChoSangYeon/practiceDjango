from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def a(request):
    return render(request, 'a.html')

def b(request):
    return render(request, 'b.html')