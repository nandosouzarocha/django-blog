from datetime import date
from django.shortcuts import render
from .models import Post

# Create your views here.

def get_date(post):
    return post['date']

all_posts = []


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] # Taking only the 3 latest posts
    return render(request, 'blog/index.html',{
        'posts': latest_posts,
    })


def posts(request):
    return render(request, 'blog/all-posts.html',{
        'posts': all_posts,
    })


def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html',{
        'post': post,
    })
