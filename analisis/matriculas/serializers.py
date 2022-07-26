from rest_framework import serializers


class TotalSerializer(serializers.Serializer):
    total = serializers.IntegerField()


class DependenciasSerializer(serializers.Serializer):
    cod = serializers.CharField()
    total = serializers.IntegerField()


class ObjetoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=2000)


