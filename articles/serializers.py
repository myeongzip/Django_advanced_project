from rest_framework import serializers
from articles.models import Article
from articles.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()   # comment의 user의 id값을 보여주는 것이 디폴트인데, 보여주는 값을 email로 바꾸고 싶을 때
    
    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Comment
        exclude = ("article",)
        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)   # 필드에 하나 넣을 때 ','를 넣지 않으면 error 발생    
        

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True)  # 정확하게 'comment_set'로 해야 제대로 작동됨. related_name을 지정해줬다면 그걸로 해야 함.
    likes = serializers.StringRelatedField(many=True)   # user의 string field로 나오게 하는 메소드(?)
    
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
    likes_count = serializers.SerializerMethodField()
    comment_set_count = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comment_set_count(self, obj):
        return obj.comment_set.count()
    
    class Meta:                 
        model = Article
        fields = ("pk", "title", "image", "updated_at", "user", "likes_count", "comment_set_count")
        
# class FeedSerializer(serializers.ModelSerializer):
#     followers = serializers.StringRelatedField(many=True)
#     article_set = ArticleListSerializer(many=True)
#     class Meta:
#         model = Article
#         fields = ("")
        
class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:                 
        model = Article
        fields = ("title", "image", "content")
        