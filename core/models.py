from django.db import models

# Create your models here.

class Posts(models.Model):
    title       = models.CharField(max_length=2000, blank=True,null=True)
    content     = models.TextField(blank=True,null=True)
    timestamp   = models.DateTimeField(auto_now_add=True,null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title