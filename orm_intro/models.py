# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    createddate = models.DateTimeField(default=datetime.now())
