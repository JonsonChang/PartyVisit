# coding=UTF-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^myVill/$', views.myVill, name='myVill'), #我認領的里
    url(r'^test_gen_db/$', views.test_gen_db, name='test_gen_db'), #建立測試DB
    
    
    url(r'^get_name/$', views.get_name, name='get_name'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
