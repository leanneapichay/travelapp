from rest_framework import serializers
from .models import *


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'


class PackingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingListItem
        fields = '__all__'


class BucketListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketListItem
        fields = '__all__'
