from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, Answer, Test, Cache
from django.contrib.auth.decorators import login_required
from itertools import count

# Create your views here.
def index(request):
	tests = Test.objects.all()
	context = {'tests': tests}
	return render(request, 'index.html', context)

@login_required
def tests(request, test_id):
	index = Cache.objects.all()[0].ind
	resul = Cache.objects.all()[0].res
	test = Test.objects.get(id=test_id)
	if request.method == 'POST':
		if request.POST.get('a'):
			if 'False' not in str(request.POST):
				Cache.objects.filter(res=resul).update(res=resul+1)
				resul += 1
			Cache.objects.filter(ind=index).update(ind=index+1)
			index += 1
		else:
			messages.error(request, 'You must choose at least 1 answer')
	else:
		Cache.objects.filter(ind=index).update(ind=0)
		Cache.objects.filter(res=resul).update(res=0)
	if index + 1  <= test.question_set.all().count():
		n = test.question_set.all()[index].id
		question = test.question_set.get(test_id=test_id, id = n)
		answers = question.answer_set.order_by('text')
		context = {'question': question, 'answers': answers, 'test':test}
		return render(request, 'tests.html', context)
	else:
		total = test.question_set.all().count()
		Cache.objects.filter(res=resul).update(res=0)
		Cache.objects.filter(ind=index).update(ind=0)
		return redirect('testing_apps:result', resul, total)
		


@login_required
def result(request, res, total):
	percent = round(((int(res) / int(total)) * 100),2)
	context = {'result': res, 'percent': percent, 'total': total}
	return render(request, 'result.html', context)


