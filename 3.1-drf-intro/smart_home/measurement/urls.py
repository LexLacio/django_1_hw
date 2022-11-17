from django.urls import path
from measurement.views import SensorsList, SensorUpdate, MeasurementsAdd

urlpatterns = [
    path('sensors/', SensorsList.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementsAdd.as_view()),
]
