from rest_framework import serializers
from .models import Car
#тоесть сериалайзе преобразовывает данные из бд в json для дальнейшего использование во вью
class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'