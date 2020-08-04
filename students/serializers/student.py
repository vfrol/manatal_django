from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import Student


class StudentCreateUpdateBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'school')

    def validate_school(self, value):
        if value.maximum_students_count == value.students_count:
            raise ValidationError(detail='There is no place in school')

        return value


class StudentSerializer(StudentCreateUpdateBaseSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'school')
        extra_kwargs = {
            'id': {'required': False}
        }


class StudentUpdateSerializer(StudentCreateUpdateBaseSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'school')
        extra_kwargs = {
            'id': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'school': {'required': False},
        }
