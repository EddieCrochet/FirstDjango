from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from django.template import loader
#only needed this to import the template
#no need after the render() method
from django.http import Http404
from .models import Question

#index method lists latest 5 questions by default now
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#before the template, and then we just returned output in the httpResponse
	#output = ', '.join([q.question_text for q in latest_question_list])
	##template = loader.get_template('polls/index.html')
	##if we didn't use the render() method we would still need above line and impott template
	context = {'latest_question_list': latest_question_list }
	return render(request, 'polls/index.html', context)
	#commented lines are what I had before we imported the template index.html
	#return HttpResponse(output)

def detail(request, question_id):
	#just a simple one line return below
	#return HttpResponse("You're looking at question %s." % question_id)
	#################3
	#try:
		#question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
		#raise Http404("Question does not exist!")
	#return render(request, 'polls/detail.html', {'question': question})
	######## above code was the first way we achieved this same thing
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
