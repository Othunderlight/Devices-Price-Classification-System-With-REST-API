from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import transaction
from .models import MobilePhone
from .serializers import MobilePhoneSerializer
from .ml_model import predict_price
from django.views import View
from django.http import HttpResponse


class HomeView(View):
    """
    View for rendering the application's home page.
    
    Methods:
        get: Returns a simple Hello World HTML response
    """
    def get(self, request):
        """Renders the home page with a simple Hello World message"""
        welcome_message = """
        <h1>Mobile Phone Price Prediction API</h1>
        <p>Welcome to the Mobile Phone Price Prediction service. This API allows you to:</p>
        <ul>
            <li>Create and manage mobile phone device records</li>
            <li>Get price range predictions (0-3) based on device specifications</li>
            <li>Query individual device details</li>
        </ul>
        <p>Price ranges:</p>
        <ul>
            <li>0: Low Cost</li>
            <li>1: Medium Cost</li>
            <li>2: High Cost</li>
            <li>3: Very High Cost</li>
        </ul>
        <p>Visit the docs to get started!</p>
        """
        return HttpResponse(welcome_message)


class MobilePhoneListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing all mobile phone devices.
    
    This view handles both listing all devices and creating new ones.
    
    Endpoints:
        GET /api/devices/: Returns a list of all mobile phone devices in the database
        POST /api/devices/: Creates a new mobile phone device entry
    
    Attributes:
        queryset: Retrieves all MobilePhone objects
        serializer_class: Uses MobilePhoneSerializer for data conversion
    """
    queryset = MobilePhone.objects.all()
    serializer_class = MobilePhoneSerializer
    
    def get(self, request, *args, **kwargs):
        """
        Retrieves a list of all mobile phone devices.
        
        Returns:
            Response: JSON array containing all device records
        """
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """
        Creates a new mobile phone device entry.
        
        Returns:
            Response: JSON object of the created device
        """
        return super().post(request, *args, **kwargs)


class MobilePhoneDetailView(generics.RetrieveAPIView):
    """
    API endpoint for viewing individual mobile phone devices.
    
    This view handles retrieving details of a specific device by its ID.
    
    Endpoint:
        GET /api/devices/{id}: Returns details of a specific device
    
    Attributes:
        queryset: Retrieves all MobilePhone objects
        serializer_class: Uses MobilePhoneSerializer for data conversion
    """
    queryset = MobilePhone.objects.all()
    serializer_class = MobilePhoneSerializer
    
    def get(self, request, *args, **kwargs):
        """
        Retrieves details of a specific mobile phone device.
        
        Args:
            kwargs: Contains the device ID in the URL
            
        Returns:
            Response: JSON object containing the device details
        """
        return super().get(request, *args, **kwargs)


@api_view(['POST'])
def predict_device_price(request, device_id):
    """
    Predicts and updates the price range for a specific mobile phone device.
    
    This endpoint:
    1. Retrieves the device by ID
    2. Prepares the device data for prediction
    3. Uses ML model to predict price range
    4. Updates the device with the predicted price
    5. Returns the updated device data
    
    Args:
        device_id: The ID of the device to predict price for
        
    Returns:
        Response: JSON object containing updated device data or error message
        
    Status Codes:
        200: Successfully predicted and updated price
        404: Device not found
        500: Internal server error during prediction
    """
    try:
        with transaction.atomic():
            # Get the device or return 404
            device = get_object_or_404(MobilePhone, pk=device_id)
            
            # Serialize device data to JSON format
            serializer = MobilePhoneSerializer(device)
            device_data = serializer.data
            
            # Remove id and price_range from the data
            device_data.pop('id', None)
            device_data.pop('price_range', None)
            
            # Call ML model to predict price using cleaned data
            predicted_price_range = predict_price(device_data)
            
            # Update device with predicted price
            device.price_range = predicted_price_range
            device.save()
            
            # Return updated device data
            return Response(serializer.data, status=status.HTTP_200_OK)
            
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

