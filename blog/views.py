
from django.shortcuts import render,get_object_or_404


from .models import Post



def starting_page(request):
    latest_post = Post.objects.all().order_by('-Date')[:3]
    
    return render(request,'blog/index.html',{'posts':latest_post,})

def posts(request):
    all_posts = Post.objects.all()
    return render(request,'blog/all-posts.html',{'all_posts':all_posts})

def post_detail(request,slug):
    identified_post = get_object_or_404(Post,Slug=slug)
    
    return render(request,'blog/post-detail.html',{'post' : identified_post,
                  'tags': identified_post.tags.all()})