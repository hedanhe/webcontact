
from django.conf.urls import url, include

from webqq import views


urlpatterns = [

    url(r'^$', views.dashboard, name='chat'),
    url(r'^(\d+)$', views.dashboard, name='chat'),

    url(r'^chat_send_msg', views.send_msg, name='chat_send_msg'),
    url(r'get_new_msg', views.get_new_msg, name='get_new_msg'),

]
