from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create'))

    class Meta:
        model = Post
        fields = '__all__'
