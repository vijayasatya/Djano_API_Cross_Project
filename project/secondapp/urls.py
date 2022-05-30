
from django.urls import path
from django.http import JsonResponse
import sys
import traceback
from django.shortcuts import render,redirect
urlpatterns = []
#from .views import cross





try:
    from .NMXV.views import cross as NMXV
except:
    pass

try:
	urlpatterns.append(path('NMXV/',NMXV,kwargs={'name':'NMXV'}))
except:
	pass