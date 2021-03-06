from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from . import serializers
from product.models import NewProduct, Category


class ProductViewSet(ModelViewSet):
    queryset = NewProduct.objects.all()
    # serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # 1й способ

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        else:
            return serializers.ProductSerializer

    # def get_permissions(self): # 2й способ
    #     if self.action in ['list', 'retrieve']:
    #         return [permissions.AllowAny(),]
    #     else:
    #         return [permissions.IsAuthenticated,]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser]
