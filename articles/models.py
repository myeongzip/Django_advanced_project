from django.db import models
from users.models import User

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')   # 이미지필드에서 null=True 가 의미없다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    # auto_created= -> 이 필드가 자동으로 생성되었는지에 대한 옵션? 
    
    def __str__(self):
        return str(self.title)