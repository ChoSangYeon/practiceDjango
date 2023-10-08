from django.shortcuts import render

def notice(request):
    return render(request, 'notice/notice.html')

def not_free(request):
    return render(request, 'notice/not_free.html')

def not_detail(request, pk):
    return render(request, 'notice/not_detail.html')

def onenone(request):
    return render(request, 'notice/onenone.html')

def one_detail(request, pk):
    return render(request, 'notice/one_detail.html')