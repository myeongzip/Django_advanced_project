from rest_framework.generics import get_object_or_404   # import 할 때 from 조심하기!
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from articles.models import Article, Comment
from articles.serializers import ArticleCreateSerializer, ArticleSerializer, ArticleListSerializer, CommentCreateSerializer, CommentSerializer

from django.db.models.query_utils import Q

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
        
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # followers.ArticleListSerializer
    def get(self, request):    # 로그인한 계정이 follow한 게시글들만 READ
        q = Q()
        for user in request.user.followings.all():  # Q object를 이용해서, 로그인한 user의 follow한 user들의 게시글 불러오기
            q.add(Q(user=user),q.OR)
        feeds = Article.objects.filter(q)       # user가 user=user에 해당하는지(로그인한 user가 follow한 user인지 확인) 확인해, 해당되는 user의 article object들을 OR 조건으로 모두 가져옴.
        serializer = ArticleListSerializer(feeds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
       
class ArticleDetailView(APIView): # /articles/{article_id}
    def get(self, request, article_id):     # detail READ
        article = get_object_or_404(Article, id=article_id)    # list READ와 차이점: all을 가져오는 게 아니라 get(id)로 해당하는 article_id 의 article하나만 가져옴
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def put(self, request, article_id):    #  detail UPDATE
        article = get_object_or_404(Article, id=article_id) # 안될 때 바로 404 띄워준다!
        if request.user == article.user:
            serializer = ArticleCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, article_id):    #  detail DELETE
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
    
    

class CommentView(APIView):    # /comment/
    def get(self, request, article_id):    # comments of certain article, list READ
        article = Article.objects.get(id=article_id)  # 이 api가 실제로 얼마나 쓰일지는 생각해불 문제다...
        comments = article.comment_set.all() # 역참조-> related_name인데, 기본값=comment_set
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def post(self, request, article_id):    # CREATE
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, article_id=article_id)   # article = Article.objetcts.get(id=article_id)인스턴스로 가져올 수도 있음.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:   
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
    
    

class CommentDetailView(APIView): # /comment/{comment_id}
    def put(self, request, article_id, comment_id):    #  comment_detail UPDATE
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentCreateSerializer(comment, data=request.data)    # content를 제외한 comment의 데이터를 바꿈
        if request.user == comment.user:
            if serializer.is_valid():
                serializer.save()    # comment의 다른 데이터(user, article_id, comment_id)를 따로 집어넣어줄 필요 없음
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
            
    def delete(self, request,article_id, comment_id):    #  comment_detail DELETE
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
            
    
    
class LikeView(APIView):    # <int:article_id>/like/
    def post(self, request, article_id):    # like
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return Response("like가 취소됐습니다.", status=status.HTTP_200_OK)
        else:
            article.likes.add(request.user)
            return Response("게시물을 like 합니다", status=status.HTTP_200_OK)