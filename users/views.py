from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from articles.models import Article
from users.models import User
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework.generics import get_object_or_404 

class UserView(APIView):
    def post(self, request):    # signup
        serializer = UserSerializer(data = request.data) # method가 post 일 때 data = request.data 지정해줘야 함.
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST) # 요청이 잘못됐기에 400이 맞음.
        
        
class CustomTokenObtainPairView(TokenObtainPairView):   # signin/login
    serializer_class = CustomTokenObtainPairSerializer
    
class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated] # 어떤 것들이 되는지 지정을 해줘야하는데, 그를 위해선 rest_framework의 permissions를 임포트해야됨.
    def get(self, request):
        return Response("get 요청!")
    
class FollowView(APIView):  # 좋아요와 로직이 비슷함. -> 좋아요 view 긁어서 약간 변형
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("unfollow 합니다.", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("follow 합니다", status=status.HTTP_200_OK)