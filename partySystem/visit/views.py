# coding=UTF-8
import time
import datetime
from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .models import address, history, people

# Create your views here.

def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': "list"}
    return render(request, 'base.html', context)
    

def myVill(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': "list"}
    return render(request, 'page_my_village.html', context)

def test_gen_db(request):
    people.objects.all().delete()
    history.objects.all().delete()
    address.objects.all().delete()
    for x in range(1,500):
        a = address(city="桃園市", area="桃園區", vil="大明里", nei="3", rd="三民路", seg= "三", lane="5", aller="6", num=x, f="4");
        a.save()
    a = address(city="桃園市", area="桃園區", vil="大明里", nei="3", rd="三民路", seg= "一", lane="5", aller="63", num="3", f="44");
    a.save()
    a = address(city="桃園市", area="中壢區", vil="小明里", nei="3", rd="青田街", num="3", f="44");
    a.save()
    a = address(city="桃園市", area="中壢區", vil="龍一里", nei="33", rd="中正路",lane="5",  num="3", f="43");
    a.save()
    a = address(city="桃園市", area="中壢區", vil="龍二里", nei="32", rd="中山路", seg= "三", aller="26", num="32", f="24");
    a.save()
    a = address(city="桃園市", area="桃園區", vil="三石里", nei="3", rd="三民路", seg= "三", lane="5", aller="6", num="3", f="34");
    a.save()
    a.history_set.create(record='很感興趣，下次再拜訪')
    d = datetime.datetime.strptime('2010-11-16 20:10:58', '%Y-%m-%d %H:%M:%S')
    a.people_set.create(birthday=d, user_id='H123456782', name="陳小姐")
    return render(request, 'page_my_village.html')
    
    
    
def get_name(request): #
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addressForm()

    return render(request, 'name.html', {'form': form, 'people_form': peopleForm, 'history_form': historyForm})    
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
