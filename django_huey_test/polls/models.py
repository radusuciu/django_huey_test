from django.db import models


class Beans(models.Model):
    count = models.IntegerField()


class Counter(models.Model):
    failed = models.BooleanField(default=False)
    succeeded = models.BooleanField(default=False)


class NotBeanCounts(models.Model):
    num = models.TextField()
