from django.forms import ModelForm
from .models import Userprofile

class UserPForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._update_field_attributes()

    def _update_field_attributes(self):
        """Update widget attributes for form fields."""
        field_classes = {
            'about': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300',
            'avatar': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300',
            'talks_about': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300',
        }
        for field_name, css_class in field_classes.items():
            self.fields[field_name].widget.attrs.update({'class': css_class})

    class Meta:
        model = Userprofile
        fields = ['about', 'avatar', 'talks_about']
        labels = {
            'about': 'Write something about you',
            'avatar': 'Profile Photo',
            'talks_about': 'Topics you talk about'
        }
