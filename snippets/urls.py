from django.urls import path
# from .serializer_views import *
from .class_base_view import *

urlpatterns = [
    path('snippets/', SnippetListView.as_view()),
    path('snippets/<pk>/', SnipperDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
