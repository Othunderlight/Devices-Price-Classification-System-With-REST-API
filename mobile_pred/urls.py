from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('api/devices/', views.MobilePhoneListCreateView.as_view(), name='device-list'),
    path('api/devices/<int:pk>/', views.MobilePhoneDetailView.as_view(), name='device-detail'),
    path('api/predict/<int:device_id>/', views.predict_device_price, name='predict-price'),
]
