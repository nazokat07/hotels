from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from apps.hotel.models import Hotel
from apps.room.models import Room
from apps.booking.models import Booking
from apps.guest.models import Guest

from .serializers import HotelSerializer
from .serializers import RoomSerializer
from .serializers import BookingSerializer
from .serializers import GuestSerializer



class HotelAPIView(APIView):

    def get(self, request):
        hotel = Hotel.objects.all()
        serializer = HotelSerializer(hotel, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = HotelSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class HotelDetailAPIView(APIView):

    def get(self, request, pk):
        flight = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(Hotel)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(Hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        flight = Hotel.objects.get(pk=pk)
        flight.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    









class RoomAPIView(APIView):

    def get(self, request):
        room = Room.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = RoomSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class RoomDetailAPIView(APIView):

    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(Room)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(Room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)






class BookingAPIView(APIView):

    def get(self, request):
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = BookingSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class BookingDetailAPIView(APIView):

    def get(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(Booking)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(Booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=HTTP_204_NO_CONTENT)


    




class GuestAPIView(APIView):

    def get(self, request):
        guest = Guest.objects.all()
        serializer = GuestSerializer(guest, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = GuestSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class GuestDetailAPIView(APIView):

    def get(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(Guest)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(Guest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=HTTP_204_NO_CONTENT)


    
