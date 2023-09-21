from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserSerializer

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data) # 꼭 data = request.data 지정해줘야 함.
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)    # 저장한 데이터들 보여주기
        else:
            print(serializer.errors)        # 개발 단계에선 error의 정보를 알면 좋지만, 실제에선 쓰면 X
            return Response({"message":f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST) # 요청이 잘못됐기에 400이 맞음.
