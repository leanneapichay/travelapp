from django.db import models
from trips.models import Trip, Stop, BucketListItem


class Journal(models.Model):
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             null=False)
    stop = models.ForeignKey(Stop,
                             on_delete=models.CASCADE,
                             null=False)
    journal = models.TextField


class ReviewBucketList(models.Model):
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             null=False)

    stop = models.ForeignKey(Stop,
                             on_delete=models.CASCADE,
                             null=False)

    bucketList = models.ForeignKey(BucketListItem,
                                   on_delete=models.CASCADE,
                                   null=True)
    review = models.TextField
