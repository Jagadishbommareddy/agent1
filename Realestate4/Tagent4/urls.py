from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AgentList.as_view(), name='agent-list'),
    url(r'agent/add/$', views.AgentAddressCreate.as_view(), name='agent-add'),
    url(r'agent/(?P<pk>[0-9]+)/$', views.AgentAddressUpdate.as_view(), name='agent-update'),

    url(r'agent/(?P<pk>[0-9]+)/delete/$', views.AgentDelete.as_view(), name='agent-delete'),
]