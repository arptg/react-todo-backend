from rest_framework import serializers
from .models import Todo, TodoLabel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'title',
            'description',
            'done',
            'label',
            'user'
        )


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoLabel
        fields = ('name', 'user')
