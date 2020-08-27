from django.http import HttpResponse
from pprint import pprint
from django.shortcuts import render


def register(request):
    return render(request, 'account/register.html')
