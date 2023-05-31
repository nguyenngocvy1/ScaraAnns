from django.urls import path
from .views import ScaraPredict

urlpatterns = [
    path('predict/', ScaraPredict.as_view(), name='predict'),
]
