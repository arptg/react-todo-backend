from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView, LabelListCreateView

urlpatterns = [
    url(r'^$', TodoListCreateView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', TodoRetrieveUpdateDestroyView.as_view()),
    url(r'^label/$', LabelListCreateView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
