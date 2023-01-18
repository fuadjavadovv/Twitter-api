from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .models import Author, Following
from .serializers import RegisterSerializer, AuthorSummarySerializer, FollowingSerializer, FollowerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.permissions import UserDetailPermission


class UserDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSummarySerializer
    permission_classes = [UserDetailPermission]
    
class UserListAV(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSummarySerializer

class RegisterAV(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = RegisterSerializer
    
@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def follow(request, pk):
    follows = get_object_or_404(Author, pk=pk)
    Following.objects.create(author=request.user.author, follows=follows)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def unfollow(request, pk):
    follower = request.user.author
    following_author = get_object_or_404(Author, pk=pk)
    follow = get_object_or_404(Following, author=follower, follows=following_author)
    follow.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

class FollowingListAV(generics.ListAPIView):
    def get_queryset(self):
        author = get_object_or_404(Author, pk=self.kwargs.get('pk'))
        followings = Following.objects.filter(author=author).order_by('-created')
        return followings
    serializer_class = FollowingSerializer

class FollowerListAV(generics.ListAPIView):
    def get_queryset(self):
        author = get_object_or_404(Author, pk=self.kwargs.get('pk'))
        followers = Following.objects.filter(follows=author).order_by('-created')
        return followers

    serializer_class = FollowerSerializer
    
    
@api_view(['POST'])
def add_block(request, pk):
    request.user.author.blockeds.add(pk)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def remove_block(request, pk):
    request.user.author.blockeds.remove(pk)
    return Response(status=status.HTTP_202_ACCEPTED)

class BlockListAV(generics.ListAPIView):
    def get_queryset(self):
        author = self.request.user.author
        return author.blockeds.all()

    serializer_class = AuthorSummarySerializer