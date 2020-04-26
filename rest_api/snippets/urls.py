from django.urls import path
from django.conf.urls import include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('api/', api_root),
    path('api/snippets/', snippet_list, name='snippet-list'),
    path('api/snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('api/snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('api/users/', user_list, name='user-list'),
    path('api/users/<int:pk>/', user_detail, name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)