from django.shortcuts import render
from django.http import HttpResponse
from cinema.models import cinema
import os, sys
import json
import random


# Create your views here.

def index(request):
    return render(request,'index.html')

def create(request):
    c = cinema.objects.create(
        names='测试影城' + str(random.randint(1, 10)),
        cinemaCode=10001 + random.randint(1, 1010),
        systemName='粤科云',
        maoyanId=101,
        taopiaopiaoId=102
    )
    c.save()
    return HttpResponse("<p>添加成功</p>")


def list(request):
    cinemalist = cinema.objects.all()
    print(cinemalist)
    return render(request, 'list.html', {'cinemalist': cinemalist})
    pass


def readerData(request):
    new_dict = []
    filepath = sys.path[0] + "/static/data/cinema.json"
    txt = open(filepath, 'r', encoding='UTF-8')
    json_dict = json.load(txt)
    # print({"cinemajson":json_dict})
    for row in json_dict["rows"]:
        
        try:
            _oldcinema = cinema.objects.get(cinemaCode=row["code"])
        except Exception as e:
            _oldcinema = None
        if _oldcinema:
            # 已经存在记录执行更新操作
            _oldcinema.names=row["name"]
            _oldcinema.cinemaCode=row["code"]
            _oldcinema.save()
            print("已经存在记录："+_oldcinema.names)
        else:
            cinema.objects.create(names=row["name"],cinemaCode=row["code"]).save()
            # 不存在记录执行更新操作
            print("不存在记录：" + row["name"]+row["code"])



        # if _oldcinema:
        #     pass
        # c = ciname.objects.create(
        #     names=row["name"],
        #     cinemaCode=row["code"]
        # )
        # c.save()

    # for item in json_dict["rows"]:
    #     print(item)
    return render(request, 'updateCinema.html', {"cinemadata": json_dict["rows"]})
    # return (request,'',str(json_dict),content_type=dict)
    pass
