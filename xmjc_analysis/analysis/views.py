'''
first page
author: Alex
site: 
'''
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
	name = request.GET['name']
	return HttpResponse(u"Welcome " + name + " to my first django page!")

def index(request):
	return render(request, 'xmjc/index.html')