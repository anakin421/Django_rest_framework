from django.urls import path, include
# from .views import PostList, PostDetail,UserList, UserDetail,CategotyList,CategoryDetail,CategoryCreate,Apiroot
from .views import CategoryViewSet, PostViewSet , UserViewSet, RegisterViewSet
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views
# from django.contrib.auth.models import User

router = DefaultRouter()
router.register(r"users",UserViewSet)
router.register(r"posts",PostViewSet)
router.register(r"categories",CategoryViewSet)
router.register(r'registration',RegisterViewSet, basename='registration')

urlpatterns = [

    # path('api/login', login),
    # path("registration/", RegisterUser.as_view(), name='registration'),
    path("",include(router.urls)),
    # path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('',Apiroot.as_view(),name='root'),
    # path('users/', UserList, name='users'),
    # path('users/<int:pk>/', UserDetail, name='user-details'),
    # path('posts/', PostList, name = "posts"),
    # path('posts/<int:pk>/', PostDetail, name= 'post-details'),
    # path('admin/categories/', CategoryCreate.as_view(),name = 'admin_category'),
    # path('categories/', CategoryList, name = "categories"),
    # path('categories/<int:pk>/', CategoryDetail, name= 'category-details'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns += [
#     path('registration/', RegisterUser.as_view(), name='registration')
# ]
