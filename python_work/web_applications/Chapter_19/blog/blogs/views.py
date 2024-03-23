from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogForm

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

def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; create data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
        
    # Display a blank invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)