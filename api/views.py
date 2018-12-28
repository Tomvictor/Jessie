from django.shortcuts import render
from core.models import *
# Create your views here.


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
)


from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from django.db.models import Q

from .serializers import PostSerializer


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    permission_classes = [AllowAny]
    serializer_class   = PostSerializer
    lookup_field       = 'pk'




class PostListAPI(CreateModelMixin, ListAPIView):
    permission_classes = [AllowAny]
    serializer_class   = PostSerializer
    queryset = Posts.objects.all()
    # lookup_field       = 'pid'

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)