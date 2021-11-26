from django.views import generic

from .models import Question


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
