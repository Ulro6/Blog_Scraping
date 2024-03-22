from django.urls import path
from . import views
from django.urls import re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings    



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
]
