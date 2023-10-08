from django.contrib import admin
from django.urls import path
from main.views import index, about, contact, account, login, logout, blog, blog1, blog2, blog3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('account/', account),
    path('account/login', login),
    path('account/logout', logout),
    path('blog/', blog),
    path('blog/1', blog1),
    path('blog/2', blog2),
    path('blog/3', blog3),
]

"""
from django.contrib import admin
from django.urls import path
from main.views import index, about, contact, login, logout, blog, blog_1, blog_2, blog_3, testnotice, testlogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('accounts/login', login),
    path('accounts/logout', logout),
    path('blog/', blog),
    path('blog/1', blog_1),
    path('blog/2', blog_2),
    path('blog/3', blog_3),
    path('testnotice/<int:pk>', testnotice),
    path('testlogin/<str:s>', testlogin),
]
"""