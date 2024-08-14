from datetime import date
from django.shortcuts import render

# Create your views here.

def get_date(post):
    return post['date']

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Bernhard Riemann",
        "date": date(2024, 8, 13),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
        """
    },
    {
        "slug": "coding-can-be-really-fun",
        "image": "coding.jpg",
        "author": "Bernhard Riemann",
        "date": date(2024, 8, 3),
        "title": "Coding can be really fun!",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
        """
    },
    {
        "slug": "a-weekend-in-the-woods",
        "image": "woods.jpg",
        "author": "Bernhard Riemann",
        "date": date(2024, 8, 14),
        "title": "A weekend in the woods.",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat similique in deserunt earum maiores esse aperiam vero et possimus, est, nostrum expedita asperiores inventore atque molestias ea aliquid odit! Aperiam?
        """
    },
]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
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
