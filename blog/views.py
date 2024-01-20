from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView,DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import CommentForms
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-Date"]
    context_object_name = "posts"

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-Date"]
    context_object_name = "all_posts"

class SinglePostView(View):
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "tags":post.tags.all(),
            "comment_form":CommentForms()
        }
        return render(request,"blog/post-detail.html",context)
    
    def post(self,request,slug):
        comment_form = CommentForms(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        context = {
            "post":post,
            "tags":post.tags.all(),
            "comment_form":CommentForms()
        }
        return render(request,"blog/post-detail.html",context)