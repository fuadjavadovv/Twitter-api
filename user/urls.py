from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterAV.as_view(), name='register'),
    path('user-list/', views.UserListAV.as_view(), name='user-list'),
    path('user-list/<int:pk>/', views.UserDetailAV.as_view(), name='user-detail'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('follow/<int:pk>/', views.follow, name='follow'),
    path('unfollow/<int:pk>/', views.unfollow, name='unfollow'),
    path('following-list/<int:pk>/', views.FollowingListAV.as_view(), name='follow-list'),
    path('follower-list/<int:pk>/', views.FollowerListAV.as_view(), name='follow-list'),
    path('block-list/', views.BlockListAV.as_view(), name='block-list'),
    path('add-block/<int:pk>/', views.add_block, name='add-block'),
    path('remove-block/<int:pk>/', views.remove_block, name='remove-block'),
]
