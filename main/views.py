# -*- coding: utf-8
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import Compliment
from django.shortcuts import render


@api_view(['POST'])
def check_compliment(request):
    response_dict = dict()
    data = request.data
    check_compliment = Compliment.objects.filter(name=data['name']).first()
    if check_compliment:
        response_dict['compliment'] = check_compliment.compliment
    else:
        compliment = Compliment.objects.filter(name='').first()
        if compliment:
            compliment.name = data['name']
            compliment.save()
            response_dict['compliment'] = compliment.compliment
        else:
            compliments = Compliment.objects.all()
            for compliment in compliments:
                Compliment.objects.create(compliment=compliment.compliment)
            compliment = Compliment.objects.filter(name='').first()
            compliment.name = data['name']
            compliment.save()
            response_dict['compliment'] = compliment.compliment
    response_dict['name'] = data['name']
    return Response(response_dict)


@api_view(['POST'])
def create(request):
    f = open('comp.txt', "r")
    str = f.read()
    list = str.split()
    for i in list:
        if len(i) > 3:
            Compliment.objects.create(compliment=i)


def index(request):
    return render(request, 'index.html')
