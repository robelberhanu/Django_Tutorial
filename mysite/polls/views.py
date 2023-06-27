from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader


 
def index(request):
    latest_question_list = Question.objects.order_by("-pup_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return HttpResponse(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(requst, question_id):
    return HttpResponse("You are voting on question %s." % question_id)