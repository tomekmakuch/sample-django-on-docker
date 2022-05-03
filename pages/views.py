"""
Pages views
"""
# from django.shortcuts import render
from django.http import HttpResponse


def home_page_view():
    """
    Home page views
    """
    return HttpResponse('Hello, World')
