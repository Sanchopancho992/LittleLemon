from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .forms import BookingForm


def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')


def book(request):
  form = BookingForm
  if request.method == 'POST':
    form = BookingForm(request.POST)
    if form.is_valid():
      form.save()
  context = {'form': form}
  return render(request, 'book.html', context)


class MenuItemView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  
class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]
  
  
  
  