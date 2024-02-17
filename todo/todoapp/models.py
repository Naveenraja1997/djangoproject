from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length = 200)
    discription = models.TextField()
    is_completed = models.BooleanField(default = False)
    
    
    