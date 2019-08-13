from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from blog.models import  Token , Expense , Income ,User
from datetime import datetime




@csrf_exempt
def submit_expense (request):
    # submit an expense
    this_token=request.POST["token"] # اپشن ریکوئست.پست دارای چند فیلد هست که ما در برنامه "پست من " ان را میفرستیم
                                     #  که یکی از اون فیلد ها "توکن" هست  که مقدار آن را داخل "دیس توکن" میریزیم
    this_amount=request.POST["amount"]   
    this_text=request.POST["text"]                              
    this_user=User.objects.filter(token__token=this_token).get() # با استفاده از "دیس توکن" یوزر مورد نظر را فیلتر میکنیم                                  
    if 'date' not in request.POST:
        this_date=datetime.now()
    Expense.objects.create (user=this_user , amount= this_amount ,text=this_text ,date=this_date )   


    print ("I'm in submit expense")
    print(request.POST)
    return JsonResponse ({
        'status':'ok',

    }, encoder=JSONEncoder)




@csrf_exempt
def submit_income (request):
    # submit an income
    this_token=request.POST["token"] # اپشن ریکوئست.پست دارای چند فیلد هست که ما در برنامه "پست من " ان را میفرستیم
                                     #  که یکی از اون فیلد ها "توکن" هست  که مقدار آن را داخل "دیس توکن" میریزیم
    this_amount=request.POST["amount"]   
    this_text=request.POST["text"]                              
    this_user=User.objects.filter(token__token=this_token).get() # با استفاده از "دیس توکن" یوزر مورد نظر را فیلتر میکنیم                                  
    if 'date' not in request.POST:
        this_date=datetime.now()
    Income.objects.create (user=this_user , amount= this_amount ,text=this_text ,date=this_date )   


    print ("I'm in submit expense")
    print(request.POST)
    return JsonResponse ({
        'status':'ok',

    }, encoder=JSONEncoder)