from rest_framework.generics import DestroyAPIView
from rest_framework import permissions
from rest_framework.response import Response
from common.models import MediaFile
from common.api_endpoints.MediaFileDelete.serializers import MediaFileDeleteSerializer


class MediaFileDestroyAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileDeleteSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())

        return Response({"message": "File deleted successfully"}, status=204)

    def perform_destroy(self, instance):
        """
        Override to delete the actual file from storage before deleting the record
        """
        if instance.file:
            instance.file.delete(save=False)
        super().perform_destroy(instance)
