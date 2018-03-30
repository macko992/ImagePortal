from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^create/$', views.image_create, name='create'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='detail'),
    url(r'^like/$', views.image_like, name='like'),
    url(r'^$', views.image_list, name='list'),
    url(r'^uploadImage', views.image_upload, name='uploadImage'),
    url(r'^ranking/$', views.image_ranking, name='create'),
    #url(r'^liked/$', views.image_ranking_like, name='like'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.tags, name='tag'),
    url(r'^tag/$', views.tag_list,name='tags'),
    url(r'^search/', include('haystack.urls')),
]
