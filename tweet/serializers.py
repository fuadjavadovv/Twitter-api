from rest_framework import serializers
from .models import Tweet
from user.serializers import AuthorSummarySerializer

class TweetSummarySerializer(serializers.ModelSerializer):
    author = AuthorSummarySerializer(required=False)
    retweet_count = serializers.IntegerField(source='retweeted_users.count', read_only=True)
    quoted_count = serializers.IntegerField(source='quoted_tweet.count', read_only=True)
    like_count = serializers.IntegerField(source='liked_users.count', read_only=True)
    class Meta:
        model = Tweet
        fields = [
            'id',
            'author',
            'content',
            'retweet_count',
            'quoted_count',
            'like_count',
            'parent_tweet',
            'image',
            'created',
        ]
        read_only_fields = [
            'id', 'created', 
        ]
        
    def create(self, validated_data):
        print(validated_data)
        author = self.context.get('author')
        content = validated_data.get('content')
        parent_tweet = validated_data.get('parent_tweet')
        quoted_tweet = validated_data.get('quoted_tweet')
        image = validated_data.get('image')
        
        new_tweet = Tweet.objects.create(
            author = author,
            content = content,
            parent_tweet = parent_tweet,
            quoted_tweet = quoted_tweet,
            image = image,
        )
        
        return new_tweet
        
        
        
# class TweetSerializer(serializers.ModelSerializer):
#     author = AuthorSummarySerializer(required=False)
#     retweet_count = serializers.IntegerField(source='retweeted_users.count', read_only=True)
#     quoted_count = serializers.IntegerField(source='quoted_tweet.count', read_only=True)
#     like_count = serializers.IntegerField(source='liked_users.count', read_only=True)
    
#     class Meta:
#         model = Tweet
#         fields = [
#             'id',
#             'author',
#             'content',
#             'retweet_count',
#             'quoted_count',
#             'like_count',
#             'image',
#             'created',
#         ]