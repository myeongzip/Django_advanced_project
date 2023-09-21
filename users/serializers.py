from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        user = super().create(validated_data)   # DB에 연결
        print(validated_data)
        
        password = user.password
        user.set_password(password) # 비밀번호 해싱 but 이 자체로는 DB에 연결되지 않아 DB엔 해싱된 비밀번호가 들어가지 않음
        user.save() # DB에 전달하고 마무리하기 위한 save
        return user