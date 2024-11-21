from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'media']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'media': forms.FileInput(attrs={
                'class': 'file',
                'type' : 'file',
                'accept': 'image/*,video/*'
            })
        }
