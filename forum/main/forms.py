from django import forms

from main.models import Topic, Post


class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ("name", "first_post", "first_post_image")
        widgets = {
            "name": forms.Textarea(attrs={"cols": 161, "rows": 1}),
            "first_post": forms.Textarea(
                attrs={
                    "cols": 161,
                    "rows": 7,
                    "id": "message",
                }
            ),
        }


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("content", "image")
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "cols": 161,
                    "rows": 7,
                    "id": "message",
                }
            ),
        }
