from django.urls import path  
from . import views

urlpatterns=[
    path('',views.index,name='posts_home'),   
    path('greet/',views.greet,name="greet_name"),
    path('posts/',views.return_all_posts,name="all_posts"),
    #here we have created a path for onr id request
    #we must specify the data type being an int followed by the id of the dict
    path('posts/<int:post_id>/',views.return_one_post, name="one_post")
]