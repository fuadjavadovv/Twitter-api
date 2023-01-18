from django.shortcuts import get_object_or_404
from rest_framework import generics, status, parsers
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from .models import Tweet
from .serializers import (
    TweetSummarySerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializers import Author, AuthorSummarySerializer
from .paginations import SubtweetPagination
from .permissions import TweetCreateUpdtePermission

# Create your views here.
class TweetListAV(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSummarySerializer
    permission_classes = [IsAuthenticated]

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_serializer_context(self):
        if self.request.method == 'GET':
            return {}
        return {'author': self.request.user.author}


class UserTweetsAV(generics.ListAPIView):
    def get_queryset(self):
        return Tweet.objects.filter(author=self.kwargs.get('user_pk'))
    serializer_class = TweetSummarySerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def like(request, tweet_pk):
    author = request.user.author
    tweet = get_object_or_404(Tweet, pk=tweet_pk)
    tweet.liked_users.add(author)
    
    return Response(status=status.HTTP_202_ACCEPTED)
@permission_classes([IsAuthenticated])

@api_view(['POST'])
def unlike(request, tweet_pk):
    author = request.user.author
    tweet = get_object_or_404(Tweet, pk=tweet_pk)
    tweet.liked_users.remove(author)
    return Response(status=status.HTTP_202_ACCEPTED)
@permission_classes([IsAuthenticated])



class UserLikedTweetsAV(generics.ListAPIView):
    def get_queryset(self):
        return Tweet.objects.filter(liked_users=self.kwargs.get('user_pk'))
    serializer_class = TweetSummarySerializer


class UsersLikedTweetAV(generics.ListAPIView):
    def get_queryset(self):
        return Author.objects.filter(liked_tweets=self.kwargs.get('tweet_pk'))
    serializer_class = AuthorSummarySerializer

class TweetDetailAV(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [TweetCreateUpdtePermission]
    lookup_url_kwarg = 'tweet_pk'
    def get_queryset(self):
        return Tweet.objects.all()
    serializer_class = TweetSummarySerializer
    
    
class AddMentionAV(generics.CreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSummarySerializer
    permission_classes=[IsAuthenticated]

    
    
class SubtweetListAV(generics.ListAPIView):
    pagination_class = SubtweetPagination
    def get_queryset(self):
        return Tweet.objects.filter(parent_tweet=self.kwargs.get('tweet_pk'))
    serializer_class = TweetSummarySerializer

    