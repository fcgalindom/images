from django.shortcuts import render ,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path not in reverse('subir'):
           return redirect('subir')












        response = self.get_response(request)



        # Code to be executed for each request/response after
        # the view is called.

        return response