from django.urls import path
from .views import *

urlpatterns = [
    path('view_post/', render_view_post),
    path('all_posts/', render_all_posts, name = 'all_posts'),
]