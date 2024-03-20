from django.shortcuts import render

def index(request):
    """The home page for Blogs."""
    return render(request, 'blogs/index.html')