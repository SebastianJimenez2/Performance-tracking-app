from rest_framework import serializers
from syncademic.models.silabo import Silabo


class SilaboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silabo
        fields = ['id_silabo', 'tema', 'prueba_kahoot', 'prueba_sentimientos', 'prueba_tema']


