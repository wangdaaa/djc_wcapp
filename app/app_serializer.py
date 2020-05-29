from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from  app.models import GameFileDB


class GameFileDBSerializer(ModelSerializer):
    image=serializers.SerializerMethodField()

    class Meta:
        model = GameFileDB
        fields = "__all__"
    def get_image(self,obj):
        # print(11111111111111)
        # print(obj.image,'iamge============')
        image=None
        if obj.image:
            image='/static/'+obj.image

        return image
            # with open(imagepath, 'rb') as f:
            #     image_data = f.read()
            #     return image_data
    # def create(self, validated_data):
    #     if 'image' in validated_data:
    #         with open(BAS)
    #
class CreateGameFileDBSerializer(ModelSerializer):

    class Meta:
        model = GameFileDB
        fields = "__all__"
