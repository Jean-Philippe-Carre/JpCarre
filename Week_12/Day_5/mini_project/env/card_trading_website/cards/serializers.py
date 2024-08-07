from rest_framework import serializers
from .models import User, Card


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'amount_of_money', 'points')


class CardSerializer(serializers.ModelSerializer):
    current_owner = Userserializer(read_only=True)
    previous_owner = Userserializer(read_only=True)

    class Meta:
        model = Card
        fields = ('id', 'name_character', 'species', 'house', 'image_url',
                  'date_of_birth', 'patronus', 'price', 'xp_points',
                  'current_owner', 'previous_owner'
                  )
