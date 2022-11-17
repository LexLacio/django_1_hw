from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# 1. Создать датчик. Указываются название и описание датчика.
class SensorsList(ListCreateAPIView):  # Специальный класс ListAPIView, работает по-умолчанию с GET запросами
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.
# 2. Изменить датчик. Указываются название и/или описание.
class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# 3. Добавить измерение. Указываются ID датчика и температура.
class MeasurementsAdd(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
