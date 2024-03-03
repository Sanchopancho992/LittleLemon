from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name='about'),
  path('book', views.book, name='book'),
  path('menu', views.MenuItemView.as_view(), name='menu'),
  path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
  path('bookings', views.BookingViewSet.as_view({'get': 'list'}), name='bookings'),
]