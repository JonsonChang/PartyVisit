# coding=UTF-8
import time
import datetime
import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .forms import *
from .models import address, history, people


def json_response(result, msg="", data={}):
#     return HttpResponse("ok")
#     return HttpResponse(json.dumps({"result": result, "msg": msg, "data": data}), mimetype='application/json')
    return HttpResponse(json.dumps({"result": result, "msg": msg, "data": data}))


# Create your views here.
def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': "list"}
    return render(request, 'base.html', context)


class myVillView(generic.list.ListView):
    paginate_by = 6
    template_name = 'page_my_village.html'
    context_object_name = 'addr_list'
     
    def get_queryset(self):
        return address.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(myVillView, self).get_context_data(**kwargs)
#         print context
        return context

        
class address_UpdateView(UpdateView):
    model = address
    fields = '__all__'
    template_name = 'page_address_detail.html'
    success_url = '/thanks/'
    
    def get_context_data(self, **kwargs):
        context = super(address_UpdateView, self).get_context_data(**kwargs)
        print context
#         print context['address'].store
#         
#         context['form'] = addressForm(context['address']) 
        return context
    
class address_DetailView(generic.DetailView):
    model = address
    template_name = 'page_address_detail.html'
    def get_context_data(self, **kwargs):
        context = super(address_DetailView, self).get_context_data(**kwargs)
        print context
        print context['address'].store
        
        context['form'] = addressForm(context['address']) 
        return context

		
def address_History(request, addr_id = 0):
    a = address.objects.get(pk=addr_id)
    h = a.history_set.all().order_by('visit_date') 
    p = a.people_set.all()
    return render(request, 'page_address_history.html', 
                  {'history_list': h, 
                   'people_list':p,
                   'address':a})

        
def people_update(request):
    if request.method == 'POST': # 更新資料 
        form = peopleForm(request.POST)
#         print request.POST
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else: #新增資料
        form = peopleForm()

    return render(request, 'name.html', {'form': form, 'people_form': peopleForm, 'history_form': historyForm})    

def history_add(request):
    result = True
    if request.method == 'POST': # 新增 / 更新資料 
        print request.POST
        form = historyForm(request.POST)
        if form.is_valid():
#             print request.POST["record"];
#             print request.POST["address"];
            a = get_object_or_404(address, pk=request.POST["address"])
            a.history_set.create(record=request.POST["record"])
            return json_response(result, msg=u'成功', data={})
        else:
            result = False
            return json_response(result, msg=u'失敗', data={})
		
def get_name(request):  #
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        print request.POST
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addressForm()

    return render(request, 'name.html', {'form': form, 'people_form': peopleForm, 'history_form': historyForm})    

def test_gen_db(request):
    people.objects.all().delete()
    history.objects.all().delete()
    address.objects.all().delete()
    
    a = address(city="桃園市", area="桃園區", vil="三石里", nei="3", rd="三民路", seg="三", lane="5", aller="6", num="3", f="34");
    a.save()    
    a.history_set.create(record='很感興趣，下次再拜訪1')
    a.history_set.create(record='很感興趣，下次再拜訪2')
    a.history_set.create(record='很感興趣，下次再拜訪3')
    a.history_set.create(record='很感興趣，下次再拜訪4')
    
    d = datetime.datetime.strptime('2011-11-16 20:10:58', '%Y-%m-%d %H:%M:%S')
    a.people_set.create(birthday=d, user_id='H123456782', name="陳小姐")		
    d = datetime.datetime.strptime('2010-2-16 20:10:58', '%Y-%m-%d %H:%M:%S')
    a.people_set.create(birthday=d, user_id='H123456732', name="陳先生")
    d = datetime.datetime.strptime('1990-4-26 20:10:58', '%Y-%m-%d %H:%M:%S')
    a.people_set.create(birthday=d, user_id='H123456742', name="陳妹妹")
    
    a = address(city="桃園市", area="桃園區", vil="大明里", nei="3", rd="三民路", seg="一", lane="5", aller="63", num="3", f="44");
    a.save()
    a = address(city="桃園市", area="中壢區", vil="小明里", nei="3", rd="青田街", num="3", f="44");
    a.save()
    a = address(city="桃園市", area="中壢區", vil="龍一里", nei="33", rd="中正路", lane="5", num="3", f="43");
    a.save()
    a = address(city="桃園市", area="中壢區", vil="龍二里", nei="32", rd="中山路", seg="三", aller="26", num="32", f="24");
    a.save()

    for x in range(1, 500):
        a = address(city="桃園市", area="桃園區", vil="大明里", nei="3", rd="三民路", seg="三", lane="5", aller="6", num=x, f="4", store="好店");
        a.save()
    
    return render(request, 'page_my_village.html')
    
    
    
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
