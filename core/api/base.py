from django.db import transaction
from rest_framework import generics, mixins


class BaseAPIView(generics.GenericAPIView,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @transaction.atomic
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
