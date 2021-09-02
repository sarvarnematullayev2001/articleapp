from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField



class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    views = models.ManyToManyField(IpModel, related_name='post_views', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment

    success_url = reverse_lazy('post_list')