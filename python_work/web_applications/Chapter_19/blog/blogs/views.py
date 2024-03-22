from django.shortcuts import render

from .models import BlogPost

def index(request):
    """The home page for Blogs."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Show all blogs."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Show a single blog."""
    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog, 'blog_text': blog.text, 'date_added': blog.date_added}
    return render(request, 'blogs/blog.html', context)