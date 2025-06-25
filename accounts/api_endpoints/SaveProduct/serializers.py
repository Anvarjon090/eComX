from rest_framework.serializers import Serializer, IntegerField


class SaveProductSerializer(Serializer):
    id = IntegerField()
