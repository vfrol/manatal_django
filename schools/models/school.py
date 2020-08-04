from django.db import models


class School(models.Model):
    name = models.CharField('School', max_length=20, unique=True)
    maximum_students_count = models.PositiveSmallIntegerField('Maximum of students')

    def __str__(self):
        return self.name

    @property
    def students_count(self):
        return self.students.all().count()
