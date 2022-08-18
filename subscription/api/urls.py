from django.urls import path
from . import views

app_name = 'api-subscription'

urlpatterns = [

     path('SubscriptionList/', views.SubscriptionList.as_view(), name='SubscriptionList')
    
]

