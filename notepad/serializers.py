from rest_framework import serializers
from .models import Notebook

class NotebookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    date = serializers.DateTimeField()

    #to create and return a new notebook  instance with the given validated data
    def create(self, validated_data):
        return Notebook.objects.create(**validated_data)

    #to update and return an existing notebook instance, given the validated_data
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date) 