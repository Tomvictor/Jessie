from django.db import models

# Create your models here.

class Posts(models.Model):
    title       = models.CharField(max_length=2000, blank=True,null=True)
    content     = models.TextField(blank=True,null=True)
    timestamp   = models.DateTimeField(auto_now_add=True,null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

    def get_timestamp(self):
    	time = self.timestamp
    	time_str = time.strftime("%Y-%m-%d %I:%M:%S %p")
    	ret = "Created on " + time_str
    	return ret

    def get_updatestamp(self):
    	time = self.last_updated
    	time_str = time.strftime("%Y-%m-%d %I:%M:%S %p")
    	ret = "Last updated on " + time_str
    	return ret