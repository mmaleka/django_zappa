from rest_framework import serializers
from subscription.models import Subscription



class SubscriptionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('id', 'email_address', 'user_message', 'user_cellnumber', )
