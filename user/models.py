from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='imgs')

    def __unicode__(self):
        return u'Student:%s'%self.sname