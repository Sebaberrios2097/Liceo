from django.urls import URLPattern, path
from Almuerzos.views import lista_almuerzos, detalle_almuerzo

urlpatterns = [
    path('lista_almuerzos', lista_almuerzos, name='lista_almuerzos'),
    path('detalle_almuerzo/<id>', detalle_almuerzo, name='detalle_almuerzo'),

]