from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from articles.models import Article
from articles.serializers import ArticleCreateSerializer, ArticleSerializer, ArticleListSerializer

class ArticleView(APIView):    # /articles/
    def get(self, request, format=None):    # list READ
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True) # many = True -> 여러 개 가져올 수 있도록 설정.
        return Response(serializer.data, status=status.HTTP_200_OK) 
        
    
    def post(self, request, format=None):    # CREATE
        serializer = ArticleCreateSerializer(data = request.data) # 꼭 data = request.data 지정해줘야 함.
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)    # 저장한 데이터들 보여주기
        else:
            print(serializer.errors)        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ArticleDetailView(APIView): # /articles/{article_id}
    def get(self, request, article_id):     # detail READ
        pass
    
    def put(self, request, article_id):    #  detail UPDATE
        pass
    
    def delete(self, request, article_id):    #  detail DELETE
        pass
    
    

class CommentView(APIView):    # /comment/
    def get(self, request):    # comments of certain article, list READ
        pass
    
    def post(self, request):    # CREATE
        pass
    
    

class CommentDetailView(APIView): # /comment/{comment_id}
    def put(self, request, article_id):    #  comment_detail UPDATE
        pass
    
    def delete(self, request, article_id):    #  comment_detail DELETE
        pass
    
    
class LikeView(APIView):    # /like/
    def post(self, request):    # like
        pass