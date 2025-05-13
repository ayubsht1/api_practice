from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # ✅ use the FK field name

    class Meta:
        model = Task
        fields = '__all__'
