from django.shortcuts import render
from .models import Post
# from django.template.loader import render_to_string
# from django.http import HttpResponse, JsonResponse
# from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, HttpResponseForbidden

def blog(request):
    db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'blog/blog.html', context)

def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'blog/post.html', context)

def test(request):
    return render(request, 'blog/test.txt')


    """
    # request => HttpRequest
    # return되는 응답값 => HttpResponse
    data = [
        {'title': 'Post 1', 'text': 'Text 1', 'pk': 1},
        {'title': 'Post 2', 'text': 'Text 2', 'pk': 2},
        {'title': 'Post 3', 'text': 'Text 3', 'pk': 3},
    ]
    # return HttpResponse('hello world') # 1
    # return HttpResponse('<h1>hello world</h1>') # 2

    s = '<h1>{{title}}</h1><p>{{text}}</p>'
    # return HttpResponse(s) # 3
    # return HttpResponse(s.replace('{{title}}', data[0]['title']).replace('{{text}}', data[0]['text'])) # 4 (그래서 내부에서 css나 js를 못읽는 것입니다.)

    header = '<h2>hell world</h2>'
    main = render_to_string('blog/test.txt', {'data': data[0]})
    footer = '<p>bye world</p>'

    '''
    blog/test.txt
    <p>hello blog</p>
    <p>{{data.title}}</p>
    <p>{{data.text}}</p>
    '''

    # return HttpResponse(header + main + footer) # 5

    # DRF, REST API
    return JsonResponse(data, safe=False) # 6
    """
