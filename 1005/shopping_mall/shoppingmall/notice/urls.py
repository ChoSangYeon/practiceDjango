from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice, name='notice.html'),
    path('free/', views.not_free, name='not_free.html'),
    path('free/<int:pk>', views.not_detail, name='not_detail.html'),
    path('onenone/', views.onenone, name='onenone.html'),
    path('onenone/<int:pk>', views.not_detail, name='one_detail.html'),
]