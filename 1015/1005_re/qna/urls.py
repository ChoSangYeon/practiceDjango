from django.urls import path
from . import views

urlpatterns = [
    path('', views.qna, name='qna'),
    path('<int:pk>/', views.qna_detail, name='qna_detail'),
]