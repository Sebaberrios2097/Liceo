from rest_framework import serializers
from Cursos.models import Almuerzo

class AlmuerzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almuerzo
        fields = ['id_almuerzo', 'nombre_almuerzo', 'descripcion_almuerzo', 'id_tipo_almuerzo']