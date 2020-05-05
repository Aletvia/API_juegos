from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Score
import json

# Create your views here.

@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)



class createScore(APIView):
    def post(self, request, *args, **kwargs):
        #TODO: Agregar seguridad para petición
        try:
            data = json.loads(request.body)
        except Exception as e:
            print (e)
            return Response({"Error": "Formato incompatible"}, status= status.HTTP_400_BAD_REQUEST)
        score=Score.create(data["juego"], data["jugador"], data["nivel"], data["tiempo"], data["fecha"])
        score.save()
        return Response(status= status.HTTP_201_CREATED)
        return Response({"Status": "Ok"}, status= status.HTTP_200_OK)
