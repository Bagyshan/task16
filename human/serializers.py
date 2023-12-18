from rest_framework import serializers
from .models import Human

class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 50:
            raise serializers.ValidationError('title length more than 50')
        return value