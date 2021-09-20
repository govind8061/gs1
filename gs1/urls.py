
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.codestack_home),
    path('stuinfo/<int:pk>/', views.student_detail),
    path('stuinfo/', views.student_list), 
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
