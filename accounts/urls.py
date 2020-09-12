from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserLogin, RegisterUser

urlpatterns = [
    url(r'^login/$', UserLogin.as_view()),
    url(r'^register/$', RegisterUser.as_view()),
    url(r'^refresh/$', TokenRefreshView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
