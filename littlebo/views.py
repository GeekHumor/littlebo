# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

def orz(request):
    return HttpResponse('小波~ 我在這！')
