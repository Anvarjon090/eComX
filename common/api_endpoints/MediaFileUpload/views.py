from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from common.models import MediaFile
from common.api_endpoints.MediaFileUpload.serializers import MediaFileUploadSerializer


class MediaFileCreateAPIView(CreateAPIView):
    """
    Create a new media file
    """

    queryset = MediaFile.objects.all()
    serializer_class = MediaFileUploadSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
