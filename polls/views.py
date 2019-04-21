from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list
    # }
    return HttpResponse(template.render(context, request))

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    current_user = request.user
    print(current_user.id)
    # If the user logged in created the question, dont allow he/she to answer it
    if current_user.id == question.user_id:
        return HttpResponse("You can't answer your own question =)")
    else:
        return render(request, 'polls/detail.html', {'question': question})
        
    # try:
    #     question = Question.objects.get(pk= question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', { 'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
@login_required
def message(request, question_id):
    candidate_message = request.POST["body_of_message"]
    question = get_object_or_404(Question, pk=question_id)
    question.message_set.create(candidate_message=candidate_message)
    # question.save()
    # return HttpResponse(candidate_message)

    return HttpResponseRedirect(
        reverse("polls:detail", args=(question.id,)))

@login_required
def create_question(request):
    return render(request, 'polls/create_question.html')

def save_question(request):
    return HttpResponse(request.POST['question_text'])


def this_is_json(request):
    return JsonResponse({"message":"Hello class", 
                        "Json":"Java Script Object Notation", 
                        "List of keyWords in Python": [{"name":"class"}, {"name":"def"}, {"name":"return"}, {"name":"try"}, {"name":"try"}] 
                        
                        })