from django.shortcuts import render

def notice(request):
    return render(request, 'notice/notice.html')

def free(request):
    return render(request, 'notice/free.html')

def free_detail(request, pk):
    return render(request, 'notice/free_detail.html')

def ono(request):
    return render(request, 'notice/ono.html')

def ono_detail(request, pk):
    return render(request, 'notice/ono_detail.html')