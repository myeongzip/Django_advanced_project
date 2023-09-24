from rest_framework import serializers
from articles.models import Article
from articles.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)   # 필드에 하나 넣을 때 ','를 넣지 않으면 error 발생    
        

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    class Meta:                 # serializer에 많은 기능이 있고 커스터마이징 가능한 기능들이 많지만, 우선 가장 간단한 버전으로 사용.
        model = Article
        fields = "__all__"

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:                 
        model = Article
        fields = ("title", "image", "content")

class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:                 
        model = Article
        fields = ("pk", "title", "image", "updated_at", "user")
        
        
class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:                 
        model = Article
        fields = ("title", "image", "content")
        