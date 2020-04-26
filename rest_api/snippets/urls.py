from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    # path('api/', views.api_root),
    # path('api/auth/', include('rest_framework.urls')),
    # path('api/snippets/', views.SnippetList.as_view()),
    # path('api/snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # path('api/snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    # path('api/users/', views.UserList.as_view()),
    # path('api/users/<int:pk>/', views.UserDetail.as_view()),
    path('api/', views.api_root),
    path('api/snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('api/snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('api/snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('api/users/',
        views.UserList.as_view(),
        name='user-list'),
    path('api/users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)