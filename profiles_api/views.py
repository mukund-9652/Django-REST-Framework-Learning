from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        """Returns a list of api features"""
        an_apiview=[
            'Uses HTTP Methods as functions (get, post, patch, put, delte)',
            'SImilar to traditional django view',
            'gives most control over app logic',
            'is mapped mannually to urls',
        ]

        return Response({
            'message' : 'Hello' , 
            'an_apiview': an_apiview ,
            })
