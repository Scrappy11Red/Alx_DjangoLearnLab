from django import forms
from .models import Post


# creating a form
class PostForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Post

        # specify fields to be used
        fields = [
            "content",
        ]