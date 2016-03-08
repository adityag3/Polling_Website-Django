from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Question
# To load the created template instead of the default template
from django.template import loader
# Create your views here.

def index(request):
	latest_question_list = Question.objets.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list' : latest_question_list
	}
	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)

	return render(request,template,context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)