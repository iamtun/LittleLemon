from django.urls import path, include
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'tables', BookingViewSet, basename='menu')

urlpatterns = [
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]