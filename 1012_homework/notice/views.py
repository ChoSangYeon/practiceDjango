from django.shortcuts import render

# Create your views here.

def notice(request):
    return render(request, 'notice/notice.html')