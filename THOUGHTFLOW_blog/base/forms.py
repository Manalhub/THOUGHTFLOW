from django import forms
from .models import Comment, Post

# Form for creating and updating posts
class POSTForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(POSTForm, self).__init__(*args, **kwargs)
        for field_name in ['title', 'body', 'image']:
            self.fields[field_name].widget.attrs.update(
                {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300'}
            )

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        labels = {
            'title': 'Title',
            'body': 'Body',
            'image': 'Image',
        }

# Form for creating and updating comments
class COMForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(COMForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300'}
        )

    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Comment',
        }

