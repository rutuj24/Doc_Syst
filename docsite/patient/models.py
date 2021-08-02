from django.db import models


# Create your models here.
class Pat(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    symptoms = models.TextField(null=True)
    prescription = models.TextField(null=True)
    date = models.DateField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    date = models.DateField()
    Slot1 = models.CharField(max_length=122, blank=True, null=True)
    Slot2 = models.CharField(max_length=122, blank=True, null=True)
    Slot3 = models.CharField(max_length=122, blank=True, null=True)
    Slot4 = models.CharField(max_length=122, blank=True, null=True)
    Slot5 = models.CharField(max_length=122, blank=True, null=True)
    Slot6 = models.CharField(max_length=122, blank=True, null=True)
    Slot7 = models.CharField(max_length=122, blank=True, null=True)
    Slot8 = models.CharField(max_length=122, blank=True, null=True)
    Slot9 = models.CharField(max_length=122, blank=True, null=True)
    Slot10 = models.CharField(max_length=122, blank=True, null=True)

    def __str__(self):
        return str(self.date)
