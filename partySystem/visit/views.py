from django.shortcuts import render
from django.http import HttpResponse

# coding=UTF-8

from .forms import *
from .models import *

# Create your views here.

def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': "list"}
    return render(request, 'base.html', context)
    

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
