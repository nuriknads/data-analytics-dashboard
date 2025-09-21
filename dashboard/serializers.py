from rest_framework import serializers
from .models import DataSet, DataRecord

class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'

class DataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecord
        fields = '__all__'
