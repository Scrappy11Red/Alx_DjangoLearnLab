from django.urls import path
from .views import post_delete_view, post_detail_view, post_list_view, post_update_view, create_post_view


urlpatterns = [
    path('<id>/delete/', post_delete_view, name=post_delete_view),
    path('<id>/update/', post_update_view, name=post_update_view),
    path('detail/', post_detail_view, name=post_detail_view),
    path('list/', post_list_view, name=post_list_view),
    path('create', create_post_view, name=create_post_view)
]