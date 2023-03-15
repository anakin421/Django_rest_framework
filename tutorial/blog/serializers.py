from rest_framework import serializers
from .models import Category, Post
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PostSerializer1(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='post-detail',read_only=True)
    class Meta:
        model = Post
        # fields = ['id','url','title','body','owner','created_at']
        fields = ['title','url']

class CategorySerializer(serializers.ModelSerializer):
    category_info = serializers.HyperlinkedIdentityField(view_name='category-detail',read_only=True)
    posts = PostSerializer1(many=True, read_only=True,source='post_set')
    class Meta:
        model = Category
        fields = ['id','title','category_info','posts','created_at']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    # owner = serializers.ReadOnlyField(source='owner.username')
    # category = serializers.StringRelatedField(many=False)
    category = serializers.SlugRelatedField(many=False,queryset=Category.objects.all(),slug_field='title')
    url = serializers.HyperlinkedIdentityField(view_name='post-detail',read_only=True)
    class Meta:
        model = Post
        fields = ['id','url','title','body','owner','category','created_at']

# class PostSerializer2(serializers.ModelSerializer):
#     category = serializers.StringRelatedField(many=False)
#     url = serializers.HyperlinkedIdentityField(view_name='post-detail',read_only=True)
#     class Meta:
#         model = Post
#         fields = ['id','url','title','body','category','created_at']


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method == "PUT":
            self.fields.pop('password')

    posts = PostSerializer1(many=True, read_only=True)
    profile = serializers.HyperlinkedIdentityField(view_name='user-detail',read_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            # password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ('id','profile','first_name','last_name','username','posts','password')

