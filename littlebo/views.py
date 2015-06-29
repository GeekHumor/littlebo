# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', RequestContext(request, locals()))

