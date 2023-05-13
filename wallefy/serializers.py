from rest_framework import serializers
from .models import BaseModel, Category, InCome, OutCome


class BaseSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = BaseModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class InComeSerializer(BaseSerializer):
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = InCome
        fields = '__all__'


class OutComeSerializer(BaseSerializer):
    category = serializers.StringRelatedField(many=False)

    def create(self, validated_data):
        
        return super().create(validated_data)
    class Meta:
        model = OutCome
        fields = '__all__'
