from django import forms
from feed.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }
