from django.urls import path
from . import views

urlpatterns = [
    path('', views.tube, name='tube'),
    path('<int:pk>/', views.post, name='post'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('tag/<str:tag>/', views.tag, name='tag'),
    path('?q=keyword/', views.keyword, name='keyword'),
]