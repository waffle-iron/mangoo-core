from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie.resources import ModelResource
from src.models import Animal
from tastypie.authorization import Authorization
from tastypie import fields


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get']
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = ApiKeyAuthentication()


class AnimalResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Animal.objects.all()
        resource_name = 'animal'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
