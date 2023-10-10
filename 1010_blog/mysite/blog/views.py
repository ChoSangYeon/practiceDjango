from django.shortcuts import render

def blog(request):
    return render(request, 'blog/blog.html')

def blog_detail(request, post_pk):
    return render(request, 'blog/blog_detail.html')

def blog_write(request):
    return render(request, 'blog/blog_write.html')

def blog_edit(request, post_pk):
    return render(request, 'blog/blog_edit.html')

def blog_del(request, post_pk):
    return render(request, 'blog/blog_del.html')

def blog_search(request):
    return render(request, 'blog/blog_search.html')

def blog_new_comt(request, post_pk):
    return render(request, 'blog/blog_new_comt.html')

def blog_up_comt(request, post_pk):
    return render(request, 'blog/blog_up_comt.html')

def blog_del_comt(request, post_pk):
    return render(request, 'blog/blog_del_comt.html')

def blog_category(request, slug):
    return render(request, 'blog/blog_category.html')

def blog_tag(request, slug):
    return render(request, 'blog/blog_tag.html')