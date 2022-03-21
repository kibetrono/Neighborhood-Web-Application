from django.forms import ModelForm
from .models import Post,Business,Contact


class ProjectUploadForm(ModelForm):
    class Meta:
        model = Post
        fields =['']

# class RatingForm(ModelForm):
#     class Meta:
#         model = Rating
#         fields =['design_rate','usability_rate','content_rate']

