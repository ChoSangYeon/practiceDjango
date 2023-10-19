from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_list = PostListView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def form_valid(self, form):
        video = form.save(commit=False)
        video.author = self.request.user
        return super().form_valid(form)

post_new = PostCreateView.as_view()


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)

post_detail = PostDetailView.as_view()


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

post_edit = PostUpdateView.as_view()


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')

    def test_func(self):
        return self.get_object().author == self.request.user

post_delete = PostDeleteView.as_view()


@login_required
def comment_new(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('tube:post_detail', pk)
        else:
            form = CommentForm()
        return render(request, 'tube/form.html', {'form': form,})