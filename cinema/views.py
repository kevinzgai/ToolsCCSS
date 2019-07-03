from django.shortcuts import render
from django.http import HttpResponse
from cinema.models import ciname
import os,sys
import json
import random
# Create your views here.


def create(request):
    c = ciname.objects.create(
        names='测试影城'+str(random.randint(1, 10)),
        cinemaCode=10001 + random.randint(1, 1010),
        systemName='粤科云',
        maoyanId=101,
        taopiaopiaoId=102
    )
    c.save()
    return HttpResponse("<p>添加成功</p>")


def list(request):
    cinemalist = ciname.objects.all()
    print(cinemalist)
    return render(request, 'list.html', {'cinemalist': cinemalist})
    pass


def readerData(request):
    new_dict=[]
    filepath=sys.path[0]+"/static/data/cinema.json"
    txt = open(filepath,'r',encoding='UTF-8')
    json_dict=json.load(txt)
    print({"cinemajson":json_dict})
    # for item in json_dict["rows"]:
    #     print(item)
    return render(request,'updateCinema.html',{"cinemadata":json_dict["rows"]})
    # return (request,'',str(json_dict),content_type=dict)
    pass
