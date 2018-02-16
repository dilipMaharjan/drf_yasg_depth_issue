from rest_framework import serializers

from .models import Todo, TodoAnother


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title',)


class TodoAnotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title',)
        depth = 2


class TodoYetAnotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title',)
        depth = 2
