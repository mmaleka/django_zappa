from rest_framework import serializers
from analytics.models import Analytics



class AnalyticsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Analytics
        fields = ('id', 'page_visited', 'user_action', )
