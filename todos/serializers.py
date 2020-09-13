from rest_framework import serializers
from .models import Todo, TodoLabel


class TodoSerializer(serializers.ModelSerializer):
    label_name = serializers.ReadOnlyField(source='label.name')

    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'description',
            'done',
            'label',
            'label_name',
            'user'
        )


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoLabel
        fields = ('name', 'user', 'id')
