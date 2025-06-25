from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema

from products.models import Product
from accounts.api_endpoints.SaveProduct.serializers import SaveProductSerializer


class SaveProductAPIView(APIView):
    queryset = Product.objects.all()
    serializer_class = SaveProductSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=SaveProductSerializer)
    def post(self, request, *args, **kwargs):
        if request.data.get("id"):
            product = get_object_or_404(Product, id=request.data["id"])

            if product in self.request.user.saved_products.all():
                self.request.user.saved_products.remove(product)
            else:
                self.request.user.saved_products.add(product)

            return Response({"detail": "Success"}, status=200)

        return Response({"detail": "Product id is required."}, status=400)
