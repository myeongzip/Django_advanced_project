from django.urls import path

from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.UserView.as_view(), name="user_view"),
    path('mock/', views.mockView.as_view(), name="mock_view"),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), # 로그인할 때 simplejwt에서 token obtain pair view를 가져와서 사용하고 있음. -> custom user를 해줘야하기에 views에서 만들어준다!
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('signin/', views.LoginView.as_view()),
]
