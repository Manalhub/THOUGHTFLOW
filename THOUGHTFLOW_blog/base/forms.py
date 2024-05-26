from django import forms
from .models import Comment, Post

class POSTForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        self.fields['body'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        self.fields['image'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        labels = {
            'about': ('Write something about you'),
            'avatar': ('Profile Photo'),
            'talks_about': ('Topics you talks about')
        }

class COMForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'text': ('Comment'),
        }
