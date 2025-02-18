from django.db import models

class Todo(models.Model):
    body = models.CharField(max_length=300)
    compiled = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50] + '...' if len(self.body) > 50 else self.body