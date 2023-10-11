from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo, name='memo'),
    path('<int:pk>/', views.m_page, name='m_page'),
    path('memodel/<int:pk>/', views.memodel, name='memodel')
]