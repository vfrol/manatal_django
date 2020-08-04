import uuid

from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          max_length=20)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey('schools.School', related_name='students',
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
