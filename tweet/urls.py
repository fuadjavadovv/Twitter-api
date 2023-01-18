from django.urls import path
from . import views

urlpatterns = [
    path('tweet-list/', views.TweetListAV.as_view(), name='tweet-list'),
    path('tweet-list/user/<int:user_pk>/', views.UserTweetsAV.as_view(), name='user-tweet-list'),
    path('like/<int:tweet_pk>/', views.like, name='like'),
    path('unlike/<int:tweet_pk>/', views.unlike, name='like'),
    path('tweet-list/user/<int:user_pk>/likes/', views.UserLikedTweetsAV.as_view(), name='user-liked-tweet-list'),
    path('tweet-list/<int:tweet_pk>/likes/', views.UsersLikedTweetAV.as_view(), name='tweet-liked-user-list'),
    path('tweet-list/<int:tweet_pk>/', views.TweetDetailAV.as_view()),
    path('tweet-list/<int:tweet_pk>/subtweets/', views.SubtweetListAV.as_view()),
]

