"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from web import views
from webqq import urls as chat_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', views.index),
    url(r'^chat/', include(chat_urls)),
    url(r'^category/(\d+)/$',views.category, name='category'),
    url(r'^article_detail/(\d+)', views.article_detail, name='article_detail'),
    url(r'^acc_logout/', views.acc_logout, name='logout'),
    url(r'^acc_login/', views.acc_login, name='login'),
    url(r'^new_article', views.new_article, name='new_article'),
    url(r'add_comment', views.add_comment, name='add_comment'),

]
