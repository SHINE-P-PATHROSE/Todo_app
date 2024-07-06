from django.db import models
class Todo(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    deadline = models.DateTimeField()

    def _str_(self):
        return self.task