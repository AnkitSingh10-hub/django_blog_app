from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    text = RichTextField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE, default=1)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE,)
    author = models.CharField(max_length=200)
    text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


