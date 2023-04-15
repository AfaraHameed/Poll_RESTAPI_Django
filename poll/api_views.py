from . models import Questions,Choice
from .serializers import QuestionSerializer,ChoiceSerializer
from rest_framework import viewsets
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
