# from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.response import Response
from .models import Post,Category
from .serializers import PostSerializer, CategorySerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions, viewsets
from .permissions import IsOwnerOrReadOnly, IsUserOwnerOrReadOnly, IsNotAuthenticate
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


# class RegisterUser(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsNotAuthenticate]

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['post']
    permission_classes = [IsNotAuthenticate]

# class PostList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,SessionAuthentication)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class CreateUserView(CreateModelMixin, GenericViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsUserOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication,SessionAuthentication)

    def get_permissions(self):
        if self.action in ['update','partial_update','destroy','list']:
            self.permission_classes = [IsUserOwnerOrReadOnly]
        elif self.action in ['create']:
            self.permission_classes = [permissions.IsAdminUser,]
        else :
            self.permission_classes = [permissions.AllowAny,]
        return super(self.__class__, self).get_permissions()




# class CategotyList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,permissions.DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes = (TokenAuthentication,SessionAuthentication)


# class CategoryCreate(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [permissions.IsAdminUser]



# class Apiroot(APIView):
#     def get(self,request,format=None):
#         response({
#         'users': reverse('users', request=request, format=format),
#         'posts': reverse('posts', request=request, format=format),
#         'categories': reverse('categories', request=request, format=format),
#         'admin-categories': reverse('admin_category', request=request, format = format)
#         })
#         if not request.user.is_authenticated:
#             response['registration'] = reverse('registration', request=request, format=format)

#         return Response(response)


# class PostList(APIView):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data) 

#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class PostDetail(APIView):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)        