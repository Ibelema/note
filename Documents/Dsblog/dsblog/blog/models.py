from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),
                     ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    #this is to send the user back to the detail page after the success of creating a new post
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.id])