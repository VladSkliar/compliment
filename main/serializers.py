from models import Compliment
from rest_framework import serializers


class ComplimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compliment
        fields = ('compliments', 'name')
