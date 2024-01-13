from django.urls import path, include
from django.contrib import admin
from django.urls import path
from pizza.api.pizza import CreatePizzaAndOrderAPIView
from pizza.api.order import TrackOrderAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pizza-order', CreatePizzaAndOrderAPIView.as_view(),
         name='create-pizza-order'),
    path('api/tracker-order/', TrackOrderAPIView.as_view(), name='track-order'),
]
