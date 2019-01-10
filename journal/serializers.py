from rest_framework import serializers
from .models import *


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'


class ReviewBucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewBucketList
        fields = '__all__'
