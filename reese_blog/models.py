from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# POST Model

class Post(models.Model):
    # This is going to be title with ONLY 100 characters that can be created
    title = models.CharField(max_length=100)
    # This is where the user will be able to create posts <No LIMITATION>
    content = models.TextField()
    # Field for when the post was created PLEASE FORMAT DateTimeField TRUE for auto
    date_posted = models.DateTimeField(default=timezone.now)
    # Field for the Username as Author of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # create a reverse function to return url as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
