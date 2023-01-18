from rest_framework.permissions import BasePermission

class TweetCreateUpdtePermission(BasePermission):
    def has_object_permission(self, request, view, tweet):
        if request.method == 'GET':
            if tweet.author.blockeds.has(request.user.author):
                return False
            else:
                return True
        elif request.method == 'DELETE':
            if request.user.is_superuser or request.user.author == tweet.author:
                return True
            else:
                return False
        else:
            if request.user.author == tweet.author:
                return True
            else:
                return False



            
        
            