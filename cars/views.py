from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets, permissions
from cars.filters import BrandFilterClass, CarFilterClass
from cars.models import Brand, Car
from cars.serializers import BrandModelSerializer, CarModelSerializer
# importando uma permissão personalizada...
from cars.permissions import CarOwnerPermission







class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    # add filtros rql
    filter_backends = [RQLFilterBackend]
    rql_filter_class = BrandFilterClass

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    # add filtros rql
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CarFilterClass
    # permissões personalizadas, elas sobrescrevem as permisssões globais...
    # permission_classes = [permissions.AllowAny] # deixa a url cars pública.
    # permissão personalizada... no caso duas regras...
    permission_classes = [permissions.DjangoModelPermissions, CarOwnerPermission,]
    
    


