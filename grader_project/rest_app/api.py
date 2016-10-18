from tastypie.resources import ModelResource
from grader_project.rest_app.models import Post
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()


class PostResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        resource_name = 'post'
        queryset = Post.objects.all()
        authorization = Authorization()