from django.urls import path
from .views import new_post,post_update,post_delete,post_detail,AddCommentView
 
urlpatterns = [
    path('newpost/', new_post, name='post_create' ),
    path('detail/<int:id>', post_detail, name='post_detail' ),
    # path('detail/<int:id>/comment', AddCommentVİew.as_view(), name='add_comment' ),
    path('update/<int:id>', post_update, name='post_update' ),
    path('detail/<int:id>/comment', AddCommentView, name='add_comment' ),
    path('delete/<int:id>', post_delete, name='post_delete' ),
    
]