from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

class ArticleView(APIView):    # /articles/
    def get(self, request):    # list READ
        pass
    
    def post(self, request):    # CREATE
        pass
        
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