from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def  get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    