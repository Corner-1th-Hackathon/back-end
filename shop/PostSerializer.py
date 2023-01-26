from rest_framework import serializers
from shop.models import Post, Tag, Post2, Post3,Post4, Post5,Post6, Post7,Post8, Post9,Post10, Post11, Post12
from .models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('post_code','date','name','letter','image','tag','address')

class Post2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Post2
        fields=('post_code2','date2','name2','letter2','image2')


class Post3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post3
        fields = ('post_code3', 'date3', 'name3', 'letter3', 'image3')


class Post4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post4
        fields = ('post_code4', 'date4', 'name4', 'letter4', 'image4')


class Post5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post5
        fields = ('post_code5', 'date5', 'name5', 'letter5', 'image5')


class Post6Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post6
        fields = ('post_code6', 'date6', 'name6', 'letter6', 'image6')


class Post7Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post7
        fields = ('post_code7', 'date7', 'name7', 'letter7', 'image7')


class Post8Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post8
        fields = ('post_code8', 'date8', 'name8', 'letter8', 'image8')


class Post9Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post9
        fields = ('post_code9', 'date9', 'name9', 'letter9', 'image9')


class Post10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post10
        fields = ('post_code10', 'date10', 'name10', 'letter10', 'image10')


class PostSerializer11(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_code11', 'date11', 'name11', 'letter11', 'image11')


class Post12Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post12
        fields = ('post_code12', 'date12', 'name12', 'letter12', 'image12')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'last_login', 'date_joined', 'is_staff')