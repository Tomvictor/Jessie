from django.shortcuts import render,get_object_or_404
from core.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
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
from django.contrib.auth import get_user_model

User = get_user_model()

# {"authKey":"jhdffadfbakdbfkjab"}
class SignInAPI(APIView):

    permission_classes = [AllowAny]

    def get(self,*args, **kwargs):
        return Response("GET method is not allowed",status = status.HTTP_400_BAD_REQUEST)

    def post(self,request,format=None):
        data = request.data
        status_code = "0"
        _message = "invalid"
        authKey = ""
        userId = 0

        try:
            username = data["email"]
            password = data["password"]
        except:
            print("unable to get params")
            status_code = "0"
            _message = "invalid input"
            resp = {
                "message": _message,
                "status" : status_code
            }
            context = {
                "authKey" : authKey,
                "userId" : userId,
                "message" : resp
            }
            return Response(context,status=status.HTTP_200_OK)

        try:
            print("check whether the user exists")
            this_user = get_object_or_404(User, username=username)
            # status_code = "0"

            if not this_user.is_active:
                _message = "Please complete email verification!"
                print(_message)
                status_code = "0"
                resp = {
                    "message": _message,
                    "status": status_code
                }
                context = {
                    "authKey": authKey,
                    "userId": userId,
                    "message": resp
                }
                return Response(context,status=status.HTTP_200_OK)

        except:
            status_code = "0"
            _message = "User does not exist"
            print(_message)
            resp = {
                "message": _message,
                "status": status_code
            }
            context = {
                "authKey": authKey,
                "userId": userId,
                "message": resp
            }
            return Response(context, status=status.HTTP_200_OK)

        # check whether user active or not



        user = authenticate(request, username=username, password=password)
        if user is not None:
            _message = "Authenticated"
            status_code = "1"
            print(_message)
            print(user)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            print(token)
            print(user.id)
            user_id = user.id

            resp = {
                "message": _message,
                "status" : status_code
            }
            context = {
                "authKey" : token,
                "userId" : user_id,
                "message" : resp
            }
            # this_serializer = JWTSerializer(data=context)
            # if this_serializer.is_valid():
            return Response(context, status=status.HTTP_200_OK)
        else:
            _message = "invalid credentials"
            status_code = "0"
            print(_message)
            resp = {
                "message": _message,
                "status": status_code
            }
            context = {
                "message" : resp,
            }
            return Response(context,status=status.HTTP_200_OK)




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



# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
