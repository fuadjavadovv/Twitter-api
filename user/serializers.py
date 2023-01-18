from rest_framework import serializers
from .models import Author, Following
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class AuthorSummarySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    
    class Meta:
        model = Author
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'bio',
            'approved',
            'profile_image',
        ]
        
class FollowingSerializer(serializers.ModelSerializer):
    follows = AuthorSummarySerializer()
    class Meta:
        model = Following
        fields = ['follows', 'created']
        
class FollowerSerializer(serializers.ModelSerializer):
    author = AuthorSummarySerializer()
    class Meta:
        model = Following
        fields = ['author', 'created']
        

class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'token']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        password = validated_data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        return user
    
    def get_token(self, user):
        token = Token.objects.get_or_create(user=user)[0].key
        return token
    
    
