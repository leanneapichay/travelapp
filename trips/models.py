from django.db import models
from accounts.models import Account


class Trip(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(Account,
                             on_delete=models.CASCADE,
                             null=False)


class Stop(models.Model):
    destination = models.CharField(max_length=100)
    departureDate = models.DateField
    returnDate = models.DateField
    duration = models.DurationField
    accommodation = models.CharField(max_length=125)
    visa = models.BooleanField

    user = models.ForeignKey(Account,
                             on_delete=models.CASCADE,
                             null=False)

    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             null=False)

class Budget(models.Model):

    # total projected budget for trip
    maxSpend = models.SmallIntegerField

    # the budgeted amounts for each category
    accommodationTarget = models.SmallIntegerField
    transportTarget = models.SmallIntegerField          # local transport
    activitiesTarget = models.SmallIntegerField
    shoppingTarget = models.SmallIntegerField

    # amount spent in each category
    accommodationSpent = models.SmallIntegerField
    transportSpent = models.SmallIntegerField
    activitiesSpent = models.SmallIntegerField
    shoppingSpent = models.SmallIntegerField

    # trip that budget is linked to
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             null=False)

    user = models.ForeignKey(Account,
                             on_delete=models.CASCADE,
                             null=False)


class Flight(models.Model):
    carrier = models.CharField(max_length=30)
    origin = models.CharField(max_length=3)
    departure = models.DateTimeField
    target = models.CharField(max_length=3)
    arrival = models.DateTimeField

    TYPE_CHOICES = (
        ('departing', 'd'),
        ('retuning', 'r'),
        ('one-way', 'o')
    )

    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    stop = models.ForeignKey(Stop,
                             on_delete=models.CASCADE,
                             null=False)


class BucketListItem(models.Model):
    name = models.CharField(max_length=300)
    complete = models.BooleanField

    # stop that bucket list is connected to
    stop = models.ForeignKey(Stop,
                             on_delete=models.CASCADE,
                             null=False)

    user = models.ForeignKey(Account,
                             on_delete=models.CASCADE,
                             null=False)


class PackingListItem(models.Model):
    name = models.CharField(max_length=300)
    complete = models.BooleanField

    # trip that packing list is connected to
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             null=False)

    user = models.ForeignKey(Account,
                             on_delete=models.CASCADE,
                             null=False)

