from datetime import date
from django.shortcuts import render
from django.http import Http404

all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image":"Mountain.jpeg",
        "author":"Basim",
        "date": date(2024, 6, 6),
        "title":"Mountains Hiking",
        "excerpt":"There's nothing like the Views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view! ",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum omnis
            quam eligendi, ipsum eaque iste tempora. Aliquid velit illum quia illo 
            atque iste sit perspiciatis eaque, officia quaerat ex voluptatum.
            
             Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum omnis
            quam eligendi, ipsum eaque iste tempora. Aliquid velit illum quia illo 
            atque iste sit perspiciatis eaque, officia quaerat ex voluptatum.
            
             Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum omnis
            quam eligendi, ipsum eaque iste tempora. Aliquid velit illum quia illo 
            atque iste sit perspiciatis eaque, officia quaerat ex voluptatum.
        """
    },
    {
        "slug":"learning-to-code",
        "image":"Coding.jpg",
        "author":"Basim",
        "date": date(2025, 7, 14),
        "title":"Programming Is Fun",
        "excerpt":"Every bug you fix teaches you something new, and that is what makes learning to code so rewarding!",
        "content": """
            Programming is like solving puzzles all day long. Every bug you
            fix teaches you something new, and every small project makes you
            a little more confident.

            Start small, stay curious and practice a little every day. You
            will be surprised how fast the basics click into place.

            The best way to learn is to build real things, so pick an idea
            you care about and start coding it today.
        """
    },
    {
        "slug":"ai-is-changing-everything",
        "image":"Ai-Wallpaper.jpeg",
        "author":"Basim",
        "date": date(2026, 8, 22),
        "title":"AI Is Changing Everything",
        "excerpt":"AI is moving faster than anyone expected, and it is already changing the way we write code and build products!",
        "content": """
            Artificial intelligence is moving faster than anyone expected.
            Tools that felt like science fiction a few years ago are now part
            of our everyday work.

            For developers, AI is a powerful assistant that can explain code,
            suggest ideas and speed up the boring parts of the job.

            The key is to stay curious, keep learning and use these tools to
            build better things, not to replace our own thinking.
        """
    }
]

def get_date(post):
    return post["date"]

# Create your views here.

def starting_page(request):
    sortes_posts = sorted(all_posts, key=get_date)
    latest_posts = sortes_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug): 
    
    # with next() function :
    # this_post = next((post for post in all_posts if post["slug"] == slug), None)
    
    # if this_post is None:
    #     raise Http404("Post not found")
    
    this_post = None
    for post in all_posts:
        if post["slug"] == slug :
            this_post = post
            break
    
    if this_post is None:
        raise Http404("Post not found")
    
    return render(request, "blog/post-detail.html", {
        "post": this_post
    })