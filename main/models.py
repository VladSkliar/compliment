# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Compliment(models.Model):
    compliment = models.CharField(max_length=100, verbose_name='Compliments')
    name = models.CharField(max_length=100, verbose_name='Name', blank=True)

    class Meta:
        verbose_name = 'Compliments'
