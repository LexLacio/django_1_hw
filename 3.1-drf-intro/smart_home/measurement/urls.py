from django.urls import path
from measurement.views import SensorsList, SensorUpdate, MeasurementsAdd, SensorView

urlpatterns = [
    path('sensors/', SensorsList.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementsAdd.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),

]
