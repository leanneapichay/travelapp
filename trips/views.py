from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


# View to create trip and all stops within it

class TripViews(APIView):

    def post(self, request, format=None):
        serializer = TripSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id, format=None):
        trip = self.get_object(id)
        serializer = TripSerializer(trip)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        trip = self.get_object(pk)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StopViews(APIView):

    def post(self, request, format=None):
        serializer = StopSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id, format=None):
        stop = self.get_object(id)
        serializer = TripSerializer(stop)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        stop = self.get_object(id)
        stop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddFlight(APIView):
    def post(self, request, format=None):
        serializer = FlightSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id, format=None):
        try:
            flight = self.get_object(id=id)
        except Flight.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FlightSerializer(flight)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetTripStops(APIView):

    def get(self, request, id,format=None):

        try:
            trip = Trip.objects.get(id=id)
        except Trip.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        def get_query(trip_input):
            stop_list = []
            for stop in Stop.objects.all:
                if stop.trip == trip_input:
                    stop_list.append(stop)
            return stops

        stops = get_query(trip)

        return Response(stops, status=status.HTTP_200_OK)


class BudgetViews(APIView):
    def post(self, request, format=None):
        serializer = BudgetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        budget = self.get_object(id)

        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketListViews(APIView):
    def post(self, request, format=None):
        serializer = BucketListItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        stop = self.get_object(id)
        stop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PackingListViews(APIView):
    def post(self, request, format=None):
        serializer = PackingListItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        stop = self.get_object(id)
        stop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




