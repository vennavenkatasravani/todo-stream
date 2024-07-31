from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Note(models.Model):
    todo = models.ForeignKey(Todo, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
