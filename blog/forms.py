from django import forms 
from .models import Comments
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ("post",)
        labels = {"user_name":"Your name","user_email":"Your email","text":"Your Comment"}

