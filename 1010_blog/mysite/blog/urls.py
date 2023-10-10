from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:post_pk>/', views.blog_detail, name='blog_detail'),
    path('write/', views.blog_write, name='blog_write'),
    path('edit/<int:post_pk>/', views.blog_edit, name='blog_edit'),
    path('delete/<int:post_pk>/', views.blog_del, name='blog_del'),
    path('?q="keyword"/', views.blog_search, name='blog_search'),
    path('<int:post_pk>/new_comment/', views.blog_new_comt, name='blog_new_comt'),
    path('update_comment/<int:comment_pk>/', views.blog_up_comt, name='blog_up_comt'),
    path('delete_comment/<int:comment_pk>/', views.blog_del_comt, name='blog_del_comt'),
    path('category/<str:slug>/', views.blog_category, name='blog_category'),
    path('tag/<str:slug>/', views.blog_tag, name='blog_tag'),
]