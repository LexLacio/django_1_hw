from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'Датчик №{self.id} - {self.name}: {self.description}'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)


