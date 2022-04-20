from rest_framework import viewsets
from rest_framework import generics
from ..models import models
from ..serializer import serializers
from rest_framework_simplejwt.authentication import JWTAuhentication

class EventsViewset(viewsets.ModelViewSet):
    authentication_classes =[JWTAuhentication]
    permission_classes = [IsAuthentication]
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventsSerializer

class EventsListGenericView(generics.ListAPIView):
     queryset = models.Events.objects.all()
     serializer_class = serializers.EventsSerializer

class EventsCreateGenericView(generics.CreateAPIView):
     queryset = models.Events.objects.all()
     serializer_class = serializers.EventsSerializer

class EventUpdateGenericView(generics.UpdateAPIView):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventsSerializer
    lookup_field = 'event_id'

class EventDeleteGenericView(generics.DestroyAPIView):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventsSerializer
    lookup_field = 'event_id'
