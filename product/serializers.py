from .models import *
from rest_framework import serializers

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            request = self.context.get('request')
            if request:
                for field in ['image_src', 'image_src1', 'image_src2', 'image_src3']:
                    if representation[field]:
                        representation[field] = request.build_absolute_uri(representation[field])
            return representation