from django.shortcuts import render

# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.views.generic import View

from django.template import RequestContext
# from system.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Office(View):
	class createNewDoc(View):
		@method_decorator(login_required)
		def get(self, request):
			context = RequestContext(request)
			return render_to_response('create/new.html', context)

		@method_decorator(login_required)
		def post(self,request):
			pass
			
	class Index(View):
		@method_decorator(login_required)
		def get(self, request):
			context = RequestContext(request)
			return render_to_response('base.html', context)
		# def post(self, request):
		# 	context = RequestContext(request)
		# 	return render_to_response('base.html', context)