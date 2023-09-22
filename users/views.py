from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer

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