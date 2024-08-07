from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from cards.views import CardsView, CardDetailsView, UserCreateView, UserProfileView, BuyCardView, SellCardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CardsView.as_view()),
    path('<int:pk>/', CardDetailsView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/', UserProfileView.as_view()),
    path('buy/', BuyCardView.as_view()),
    path('sell/', SellCardView.as_view()),
]
