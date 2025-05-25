from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)  # Blog title
    content = models.TextField()  # Full blog content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when last updated

    def __str__(self):
        return self.title