from dj_rql.filter_cls import AutoRQLFilterClass, FilterLookups
from cars.models import Brand, Car


class BrandFilterClass(AutoRQLFilterClass):
    MODEL = Brand
    
class CarFilterClass(AutoRQLFilterClass):
    MODEL = Car
    # personalizando o filtro, permite que a busca seja feita pelos nomes dos campos e não pelos id's
    FILTERS = [
        {
            'filter': 'brand',
            'source': 'brand__name',
        },
        {
            'filter': 'owner',
            'source': 'owner__username',
        },
    ]