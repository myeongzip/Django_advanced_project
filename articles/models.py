from django.db import models
from users.models import User

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # user._set -> 특정 user가 쓴 모든 글 불러오기
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')   # 이미지필드에서 null=True 가 의미없다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    # auto_created= -> 이 필드가 자동으로 생성되었는지에 대한 옵션? 
    likes = models.ManyToManyField(User, related_name="like_articles")   # manytomany는 related_name 설정해주는 것이 좋다. user의 related_name을 따로 설정하지 않았기에, 역참조 이름이 지금 중복되기에, related_name을 설정해야 함.
    
    def __str__(self):
        return str(self.title)
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.content)