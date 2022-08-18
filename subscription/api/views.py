from rest_framework import generics, mixins
from rest_framework.views import APIView


from subscription.models import Subscription
from . serializers import SubscriptionSerializers



class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers