from rest_framework import serializers

class EvolucionSerializer(serializers.Serializer):
    anio = serializers.IntegerField()
    total = serializers.IntegerField()
    est_urbanos = serializers.IntegerField()
    est_rurales = serializers.IntegerField()
    est_activos = serializers.IntegerField()
    est_receso = serializers.IntegerField()
    est_inactivos = serializers.IntegerField()
    
