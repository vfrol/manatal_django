from rest_framework import viewsets, mixins

from common.mixins import ActionSerializerViewSetMixin
from schools.models import School
from schools.serializers import (
    SchoolSerializer, SchoolUpdateSerializer
)


class SchoolViewSet(ActionSerializerViewSetMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = School.objects.all()
    permission_classes = []
    serializer_classes = {
        ('list', 'retrieve', 'create', 'destroy'): SchoolSerializer,
        ('update', 'partial_update'): SchoolUpdateSerializer,
    }
    filterset_fields = ['name', 'maximum_students_count']
    search_fields = ['name']
