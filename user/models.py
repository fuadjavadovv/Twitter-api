from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    bio = models.TextField(default='', blank=True)
    approved = models.BooleanField(default=False)
    blockeds = models.ManyToManyField('self')
    hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.first_name

class Following(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    follows = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='followings')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author.user.first_name} follows {self.follows.user.first_name}'
    
