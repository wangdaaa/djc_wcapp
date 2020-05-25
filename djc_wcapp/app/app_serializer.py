from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from  app.models import GameFileDB


class GameFileDBSerializer(ModelSerializer):

    class Meta:
        model = GameFileDB
        fields = "__all__"