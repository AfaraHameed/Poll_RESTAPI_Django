from django.shortcuts import render,redirect
from django.views import generic
from .models import Questions,Choice
from .mixins import RequireLoginMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.views import LoginView

# Create your views here.

"""
def index(request):
    latest_question_list = Questions.object.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html')
"""

class IndexView(RequireLoginMixin,generic.ListView):
    
    login_url = "/poll/login/"
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.order_by('-pub_date')[:5]
    

class MyCustomLoginView(LoginView):
    template_name='login.html'
    
"""
def detail(request,question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})
"""

class DetailView(generic.DetailView):
    model = Questions
    template_name = 'detail.html'
    context_object_name = 'question'


class DeleteView(generic.DeleteView):
    model = Questions
    success_url = "/"

class VoteView(generic.View):
    def get_queryset(self,choice_id):
        return Choice.objects.get(pk=choice_id)
    
    def post(self,request,pk):
        question_id = pk
        choice_id = request.POST.get('choice',None)
        try:
            queryset = self.get_queryset(choice_id)
        except(KeyError,Choice.DoesNotExist):
            return redirect('detail',pk=question_id)
        else:
            queryset.votes+=1
            queryset.save()
            return redirect('results',pk=question_id)
        

class ResultsView(TemplateResponseMixin,generic.View):
    template_name='results.html'

    def get_quesryset(self,question_id):
        return Questions.objects.get(pk=question_id)
    
    def get(self,request,pk):
        queryset = self.get_quesryset(pk)
        question =  Questions.objects.get(pk=pk)
        context={'question':queryset}
        # print(question.choice_set.all())
        return self.render_to_response(context)


