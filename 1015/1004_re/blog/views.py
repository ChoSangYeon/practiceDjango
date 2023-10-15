from django.shortcuts import render

def blog(request):
    return render(request, 'blog/blog.html')

def post(request, pk):
    return render(request, 'blog/post.html')