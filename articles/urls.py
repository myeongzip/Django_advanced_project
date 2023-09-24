from django.urls import path

from articles import views


urlpatterns = [
    path('', views.ArticleView.as_view(), name="article_view"),
    path('<int:article_id>/',views.ArticleDetailView.as_view(), name="article_detail_view"),
    path('<int:article_id>/comment/', views.CommentView.as_view(), name="comment_view"), # '<int:article_id>/comment/'로 하는 방법도 있지만, body 안에 article_id를 보내고자 함.
    path('<int:article_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name="comment_detail_view"),  # article_id가 빠져도 되지만, 통일성을 위해 유지함.
    path('<int:article_id>/like/', views.LikeView.as_view(), name="like_view"), # 좋아요 기능 = 내용이 빠진 댓글이라고 생각하자. 내용 없는 댓글을 세주는 것처럼 좋아요 개수도 세주면 됨.
]
