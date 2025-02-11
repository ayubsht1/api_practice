from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Correct the field name to 'owner'
    class Meta:
        model = Task
        fields = '__all__'
