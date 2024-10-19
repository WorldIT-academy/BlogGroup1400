from django.urls import path
from .views import *

urlpatterns = [
    path('all_authors/', render_all_authors, name = 'all_authors'),
    path('view_author/', render_view_author)
]
