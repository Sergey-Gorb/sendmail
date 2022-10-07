# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ServiceUsers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    STATUSES = (
        ('N', 'New'),
        ('P', 'Pending'),
        ('S', 'Send'),
    )
    subject = models.CharField(max_length=150)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUSES, default='N')
    created_date = models.DateTimeField(auto_created=True)
    sender = models.ForeignKey(ServiceUsers, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Issue(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=50, primary_key=True)
    birthday = models.DateField()

    def __str__(self):
        return self.email


class Subscription(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    date_send = models.DateTimeField()
    date_open = models.DateTimeField()
