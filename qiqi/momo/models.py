# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import MySQLdb
import qiqi.settings

class MomoTest(models.Model):
    runoob_title = models.CharField(max_length=20)
    runoob_author = models.CharField(max_length=20)
    submission_date = models.CharField(max_length=20)
    runoob_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'momo_test'


class RunoobTbl(models.Model):
    runoob_id = models.AutoField(primary_key=True)
    runoob_title = models.CharField(max_length=100)
    runoob_author = models.CharField(max_length=40)
    submission_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runoob_tbl'

    def __str__(self):
        return self.runoob_title
