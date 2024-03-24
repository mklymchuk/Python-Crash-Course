"""Define URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Hoem page
    path('', views.index, name='index'),
    
    # Page that shows all blogs.
    path('blogs/', views.blogs, name='blogs'),
    
    # Detail page for a single blog.
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    
    # Page for adding a new blog
    path('new_blog/', views.new_blog, name="new_blog"),
    
    # Page for editing blog.
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]
