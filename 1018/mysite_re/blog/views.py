from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import PostSerializer

# FBV
@api_view(['GET', 'POST'])
def postlist(request):
    if request.method == 'GET':
        postlist = Post.objects.all()
        serializer = PostSerializer(postlist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# CBV
# class LicatView(APIView):
#     def get(self, request):
#         posts = [
#             {'title':'1', 'content':'111'},
#             {'title':'2', 'content':'222'},
#             {'title':'3', 'content':'333'},
#         ]
#         serializer = posts
#         return Response(serializer)

# postlist = LicatView.as_view()