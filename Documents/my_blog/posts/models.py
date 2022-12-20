from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        if len(self.body)  > 50:
            return self.body[:50] + '...'

        else:
            return self.body

    class Meta:
        verbose_name_plural = 'articles'