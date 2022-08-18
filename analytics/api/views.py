from rest_framework import generics, mixins
from rest_framework.views import APIView


from analytics.models import Analytics
from . serializers import AnalyticsSerializers



class AnalyticsList(generics.ListCreateAPIView):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializers

