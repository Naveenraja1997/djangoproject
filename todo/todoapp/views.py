from rest_framework import generics
from .models import ToDoItem
from .serializers import ToDoItemsSerializer

class ToDoDetail(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemsSerializer
    
class ToDoUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemsSerializer