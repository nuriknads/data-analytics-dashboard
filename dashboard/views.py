from rest_framework import viewsets
from .models import DataSet, DataRecord
from .serializers import DataSetSerializer, DataRecordSerializer

class DataSetViewSet(viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer

class DataRecordViewSet(viewsets.ModelViewSet):
    queryset = DataRecord.objects.all()
    serializer_class = DataRecordSerializer
