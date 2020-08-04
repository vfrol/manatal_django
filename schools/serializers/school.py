from rest_framework import serializers

from schools.models import School
from students.serializers import StudentSerializer


class SchoolSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, required=False)
    students_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = School
        fields = ('id',
                  'name',
                  'maximum_students_count',
                  'students',
                  'students_count')
        extra_kwargs = {
            'id': {'required': False},
            'students': {'required': False},
            'students_count': {'required': False},
        }


class SchoolUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'maximum_students_count')
        extra_kwargs = {
            'id': {'required': False},
            'name': {'required': False},
            'maximum_students_count': {'required': False},
        }
