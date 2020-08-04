from rest_framework import exceptions


class ActionSerializerViewSetMixin(object):
    """
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('list', ): MyModelListViewSerializer,
        ('create', 'update'): MyModelCreateUpdateSerializer
    }
    """
    serializer_classes = None

    def get_serializer_class(self):
        assert self.serializer_classes is not None, (
                'Expected viewset %s should contain serializer_classes '
                'to get right serializer class.' %
                (self.__class__.__name__,)
        )
        for actions, serializer_cls in self.serializer_classes.items():
            if self.action in actions:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)
