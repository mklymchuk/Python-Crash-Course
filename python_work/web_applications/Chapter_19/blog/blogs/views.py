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
    context = {
        'blog': blog,
        'blog_title': blog.title,
        'blog_text': blog.text,
        'date_added': blog.date_added,
        }
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()  # Save the form and get the saved blog object
            # Redirect to the 'blog' URL with the blog's ID as an argument
            return redirect('blogs:blog', blog_id=blog.id)
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def edit_blog(request, blog_id):
    """Edit an existing blog."""
    blog = BlogPost.objects.get(id=blog_id)
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current blog.
        form = BlogForm(instance=blog)
    else:
        # POST data submitted; process data.
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/blog_edit.html', context)