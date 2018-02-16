from rest_framework import viewsets

from .models import Todo, TodoAnother, TodoYetAnother
from .serializer import TodoSerializer, TodoAnotherSerializer, TodoYetAnotherSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoAnotherViewSet(viewsets.ModelViewSet):
    queryset = TodoAnother.objects.all()
    serializer_class = TodoAnotherSerializer


class TodoYetAnotherViewSet(viewsets.ModelViewSet):
    queryset = TodoYetAnother.objects.all()
    serializer_class = TodoAnotherSerializer
