from rest_framework import generics
from .models import Todo
from .serializers import TodoSeializer

class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSeializer

class DetailTodo(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSeializer