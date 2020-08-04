from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from common.mixins import ActionSerializerViewSetMixin
from students.models import Student
from students.serializers import (
    StudentUpdateSerializer, StudentSerializer
)


class StudentViewSet(ActionSerializerViewSetMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Student.objects.all()
    permission_classes = []
    serializer_classes = {
        ('list', 'retrieve', 'create', 'destroy'): StudentSerializer,
        ('update', 'partial_update'): StudentUpdateSerializer,
    }
    filterset_fields = ['first_name', 'last_name', 'school']
    search_fields = ['first_name', 'last_name', 'school_name']

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if kwargs.get('school_pk'):
            data.update({'school': kwargs['school_pk']})

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        if kwargs.get('school_pk'):
            data.update({'school': kwargs['school_pk']})

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
