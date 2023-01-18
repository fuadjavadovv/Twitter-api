from django.db import models
from user.models import Author

# Create your models here.

class Tweet(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    parent_tweet = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='subtweets', default=None)
    retweeted_users = models.ManyToManyField(Author, related_name='retweets')
    quoted_tweet = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, default=None)
    show_count = models.BigIntegerField(default=0)
    liked_users = models.ManyToManyField(Author, related_name='liked_tweets')
    image = models.ImageField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']