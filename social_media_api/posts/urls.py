from django.urls import path
from .import views


urlpatterns = [
    path('<id>/delete/', views.post_delete_view, name='post_delete_view'),
    path('<id>/update/', views.post_update_view, name='post_update_view'),
    path('detail/', views.post_detail_view, name='post_detail_view'),
    path('list/', views.post_list_view, name='post_list_view'),
    path('create', views.create_post_view, name='create_post_view'),
    path('', views.CommentOverview, name='home'),
    path('create/', views.create_comments, name='create-comments'),
    path('all/', views.view_comments, name='view-comments'),
    path('update/<int:pk>/', views.update_comments, name='update-comments'),
    path('comment/<int:pk>/delete/', views.delete_comments, name='delete-comments'),
]