from django.db import models
import uuid


class Todo(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    do_by = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)
    unique_number = models.CharField(default=uuid.uuid4(), max_length=400)
    objects = models.Manager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "todo titled \"{}\"".format(self.name)
