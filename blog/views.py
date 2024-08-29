from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] # Taking only the 3 latest posts
    return render(request, 'blog/index.html',{
        'posts': latest_posts,
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html',{
        'posts': all_posts,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html',{
        'post': post,
    })
