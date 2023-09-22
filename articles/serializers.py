from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:                 # serializer에 많은 기능이 있고 커스터마이징 가능한 기능들이 많지만, 우선 가장 간단한 버전으로 사용.
        model = Article
        fields = "__all__"

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:                 # serializer에 많은 기능이 있고 커스터마이징 가능한 기능들이 많지만, 우선 가장 간단한 버전으로 사용.
        model = Article
        fields = ("title", "image", "content")

class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:                 # serializer에 많은 기능이 있고 커스터마이징 가능한 기능들이 많지만, 우선 가장 간단한 버전으로 사용.
        model = Article
        fields = ("pk", "title", "image", "updated_at", "user")
        