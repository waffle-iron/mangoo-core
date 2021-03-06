from __future__ import unicode_literals

from django.db import models


class Animal(models.Model):
    """
    Dummy model to test (see tests.py)
    """
    name = models.CharField(max_length=255)
    sound = models.CharField(max_length=255)

    def speak(self):
        return 'The '+self.name+' says "'+self.sound+'"'
