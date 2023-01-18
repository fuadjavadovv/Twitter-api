from rest_framework.permissions import BasePermission
from rest_framework import permissions


class UserDetailPermission(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     if request.method == 'DELETE':
    #         return request.user.is_superuser
    #     if request.method == 'PUT':
    #         return request.user
    def has_object_permission(self, request, view, obj):
   
      if request.method =='GET':
       return request.user.author ==obj.user