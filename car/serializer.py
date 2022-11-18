from rest_framework import serializers

from car.models import Car

class CarSerializer(serializers.ModelSerializer):
    color = serializers.ChoiceField(choices=["red"])
    class Meta: 
        model = Car
        fields = ('name', 'color', 'brand')
