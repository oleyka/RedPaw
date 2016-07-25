# from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
import pytz

from .models import Choice, Question


class IndexView(generic.ListView):  # pylint: disable=too-many-ancestors
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):  # pylint: disable=too-many-ancestors
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):  # pylint: disable=too-many-ancestors
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'polls/template.html', {'timezones': pytz.common_timezones})
