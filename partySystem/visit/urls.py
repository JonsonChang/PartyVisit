# coding=UTF-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^myVill/$', views.myVillView.as_view(), name='myVill'), #我認領的里
    url(r'^myVill/(?P<page>[0-9]+)/$', views.myVillView.as_view(), name='myVill'), #我認領的里
    url(r'^address_History/(?P<addr_id>[0-9]+)/$', views.address_History , name='address_History'),
    url(r'^address_DetailView/(?P<pk>[0-9]+)/$', views.address_UpdateView.as_view(), name='address_detail'),
    url(r'^history_add/$', views.history_add, name='history_add'),  # 新增拜訪記錄  ajax
    url(r'^people_add/$', views.people_add, name='people_add'),  # 新增人圓資料  ajax
    url(r'^people_update/$', views.people_update, name='people_update'),
    url(r'^people_form/(?P<people_id>[0-9]+)/$', views.people_modify_form , name='people_modify_form'),
    url(r'^test_gen_db/$', views.test_gen_db, name='test_gen_db'),  # 建立測試DB
    
    
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
