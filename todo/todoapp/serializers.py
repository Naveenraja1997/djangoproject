from rest_framework import serializers
from .models import ToDoItem


class ToDoItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = "__all__"
