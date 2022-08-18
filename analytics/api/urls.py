from django.urls import path
from . import views

app_name = 'api-analytics'

urlpatterns = [

     path('AnalyticsList/', views.AnalyticsList.as_view(), name='AnalyticsList')
    
]

