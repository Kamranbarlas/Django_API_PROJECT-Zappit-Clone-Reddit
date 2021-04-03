from django.contrib import admin
from django.urls import path , include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts', views.PostList.as_view()),
    path('api/posts/<int:pk>', views.Post_ko_destroy.as_view()),
    path('api/posts/<int:pk>/vote', views.CreateVote.as_view()),
    path('api-auth/',include('rest_framework.urls')),
    # path('', views.CreateVote.as_view()),
]