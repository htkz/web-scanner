# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from momo.models import *
import json


def index(request):
    return render(request, 'index.html')

def get_elements_from_db(request):
    runoob=list(RunoobTbl.objects.values('runoob_title', 'runoob_author', 'submission_date'))
    print(runoob)
    elements = dict(runoob=runoob)
    return JsonResponse(elements)
