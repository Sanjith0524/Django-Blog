from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption
    


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Post(models.Model):
    title=models.CharField(max_length=50)
    excerpt=models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts",null=True)
    Date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=50,unique=True,db_index=True)
    Content  = models.TextField(validators=[MinLengthValidator(10)])
    author  = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name='posts',null=True)
    tags = models.ManyToManyField(Tag)


class Comments(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    text = models.TextField(max_length=200)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
