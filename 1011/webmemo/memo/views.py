from django.shortcuts import render, redirect
from .models import Post

def memo(request):
    db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'memo/memo.html', context)

def m_page(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'memo/m_page.html', context)

def memodel(request, pk):
    q = Post.objects.get(pk=pk)
    q.delete()
    return redirect('memo')