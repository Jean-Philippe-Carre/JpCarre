from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from .models import Cards
from .serializers import CardsSerializer, CardDetailsSerializer, UserCreateSerializer, UserProfileSerializer, BuyCardSerializer, SellCardSerializer


# fro
# m rest_framework import generics
# from generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from rest_framework import viewsets

# Create your views here.


class CardsView(ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer


class CardDetailsView(RetrieveAPIView):
    queryset = CardDetails.objects.all()
    serializer_class = CardDetailsSerializer


class UserCreateView(CreateAPIView):
    queryset = UserCreate.objects.all()
    serializer_class = UserCreateSerializer


class UserProfileView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class BuyCardView(CreateAPIView):
    queryset = BuyCard.objects.all()
    serializer_class = BuyCardSerializer


class SellCardView(CreateAPIView):
    queryset = SellCard.objects.all()
    serializer_class = (SellCardSerializer,)
