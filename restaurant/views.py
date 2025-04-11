from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemAPIView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes=[IsAuthenticated]
    
class SingleMenuItemAPIView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
     