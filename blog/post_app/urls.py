from django.urls import path
from .views import *

urlpatterns = [
    path('view_post/<int:pk>', render_view_post, name= 'view_post'),
    path('all_posts/', render_all_posts, name = 'all_posts'),
]