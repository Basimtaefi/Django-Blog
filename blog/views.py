# from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

# all_posts = [
    
# ]

def get_date(post):
    return post["date"]

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug): 
    
    # with next() function :
    # this_post = next((post for post in all_posts if post["slug"] == slug), None)
    
    # if this_post is None:
    #     raise Http404("Post not found")
    
    this_post = get_object_or_404(Post, slug=slug)
    if this_post is None:
        raise Http404("Post not found")
    
    return render(request, "blog/post-detail.html", {
        "post": this_post,
        "post_tags": this_post.tags.all() # Solving the issue of for block tags in post-detail.html
    })