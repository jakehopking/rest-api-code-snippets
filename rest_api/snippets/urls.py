from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('api/auth/', include('rest_framework.urls')),
    path('api/snippets/', views.SnippetList.as_view()),
    path('api/snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('api/users/', views.UserList.as_view()),
    path('api/users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)