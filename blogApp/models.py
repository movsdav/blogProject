from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, default="Default Title")
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post number: {self.id}"
