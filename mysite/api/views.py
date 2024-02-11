from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from users.models import Pet, Profile
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse


@api_view(['GET'])
def get_users(request):
    if request.user.is_authenticated:
        user_profiles = Profile.objects.all()
        serializer = ProfileSerializer(user_profiles, many=True)
    else:
        raise PermissionDenied(
            "You do not have the permission to access this resource")
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_user_by_id(request, id):
    if not request.user.is_authenticated:
        user_obj = get_object_or_404(User, pk=id)
        user_profile = get_object_or_404(Profile, user=user_obj)
        if request.method == 'PUT':
            for key, val in request.data.items():
                if hasattr(user_profile, key):
                    setattr(user_profile, key, val)
                else:
                    raise Http404(
                        f'Attribute {key} does not exist in users profile')
            user_profile.save()
        elif request.method == 'DELETE':
            user_obj.delete()
    else:
        raise PermissionDenied(
            "You do not have the permission to access this resource")
    serializer = ProfileSerializer(user_profile)
    return Response(serializer.data)
