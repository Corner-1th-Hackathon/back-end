from rest_framework import serializers
from shop.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('post_code','date','name','letter','image')