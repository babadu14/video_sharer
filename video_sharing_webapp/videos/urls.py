from django.urls import path
from videos.views import Index, CreateVideo, DetailVideo, UpdateVideo, DeleteVideo, VideoCategory, SearchVideo

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', CreateVideo.as_view(), name='video-create'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update/', UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete',DeleteVideo.as_view(), name='video-delete' ),
    path('category/<int:pk>', VideoCategory.as_view(), name='category-list'),
    path('search/', SearchVideo.as_view(), name='video-search'),

]