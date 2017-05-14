from rest_framework import serializers


class GeoJSONSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField(max_length=256)
    features = serializers.ListField(read_only=True)
