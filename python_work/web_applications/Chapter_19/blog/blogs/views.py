from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """The home page for Blogs."""
    return render(request, 'blogs/index.html')

@login_required
def blogs(request):
    """Show all blogs."""
    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def blog(request, blog_id):
    """Show a single blog."""
    blog = BlogPost.objects.get(id=blog_id)
    check_blog_owner(request, blog)    
    context = {
        'blog': blog,
        'blog_title': blog.title,
        'blog_text': blog.text,
        'date_added': blog.date_added,
        }
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()  # Save the form and get the saved blog object
            # Redirect to the 'blog' URL with the blog's ID as an argument
            return redirect('blogs:blog', blog_id=new_blog.id)
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blog(request, blog_id):
    """Edit an existing blog."""
    blog = BlogPost.objects.get(id=blog_id)
    check_blog_owner(request, blog)    
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

def check_blog_owner(request, blog):
    """Check actual blog owner."""
    # Make sure the blog belongs to the current user.
    if blog.owner != request.user:
        raise Http404