from rest_framework import viewsets
from rest_framework.response import Response
from GeoFence.serializers import *
from GeoFence.models import *


# ViewSets define the view behavior.
class GetGeoFences(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = GeoJSONSerializer

    def list(self, request):
        serializer = GeoJSONSerializer(instance=locations.values(), many=True)
        return Response(serializer.data)
