from django import forms

from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text' : '', 'title': 'Title'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
            'title': forms.TextInput(attrs={'size': 40})
            }