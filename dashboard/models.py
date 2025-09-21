from django.db import models

class DataSet(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class DataRecord(models.Model):
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
