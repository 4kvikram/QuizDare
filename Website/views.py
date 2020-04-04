from django.shortcuts import render
from django.http import HttpRequest,request,HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Questions,UserAnswer,Register,FriendsAnswer,contactus
# Create your views here.



def Index(request,id=0):
    #print("page")
    if id==0:
        return render(request,'index.html',{"name":"vikraasdfadm"})
    else:
        return render(request,"index.html",{"name":"vikram"})


def Selectquestion(request):
    return render(request,'Selectquestion.html')

def getAllQuestionAndOptions(request):
    try:
        #countryList=Country.objects.all().objects.values_list('id', 'headline')
        countryList = serializers.serialize("json",Questions.objects.all())
        if countryList!="":            
            data = {
                    'success':True,
                    'message':"Data found",
                    'data':countryList }
            return JsonResponse(data) 
        else:
            data = {
                'success':False,
                'message':"data not found",
                'data':"" }
            return JsonResponse(data)
    except Exception as ex:
        #print("error is :",ex)
        return {'message':ex}

def AddUserAndQuestion(request):
    try:
        name=request.POST["name"]
        option=request.POST["Option"]
        option=option.rstrip(',')
        questionids=request.POST["Question"]
        questionids=questionids.rstrip(',')

        finalOption=option.split(',')
        finalquestionids=questionids.split(',')
        #print("data get :",name,finalOption,finalquestionids)
        
        register=Register()
        register.name=name
        register.role=2
        register.isActive=True
        register.save()
        for i in range(len(finalOption)):
            userAnswer=UserAnswer()
            userAnswer.QuID=finalquestionids[i]
            userAnswer.Questions=Questions.objects.get(id=finalquestionids[i]) 
            userAnswer.userAns=finalOption[i]
            userAnswer.Register=register
            userAnswer.isActive=True
            userAnswer.save()

        #pp=serializers.serialize("json",register)
        data = {
                'success':True,
                'message':"Data found",
                'data':register.pk
                }
        return JsonResponse(data) 
        # else:
        #     data = {
        #         'success':False,
        #         'message':"data not found",
        #         'data':"" }
        #     return JsonResponse(data)
    except Exception as ex:
        #print("error is :",ex)
        return {'message':ex}




def getUserQuestions(request):
    try:
        #countryList=Country.objects.all().objects.values_list('id', 'headline')
        id=request.GET["id"]
        #print("id is ",id)
        newData=serializers.serialize("json",UserAnswer.objects.filter(Register__pk__exact=id))
        #print(newData) 
        if newData!="":            
            data = {
                    'success':True,
                    'message':"Data found",
                    'data':newData }
            return JsonResponse(data) 
        else:
            data = {
                'success':False,
                'message':"data not found",
                'data':"" }
            return JsonResponse(data)
    except Exception as ex:
        #print("error is :",ex)
        return {'message':ex}



def saveResult(request):
    try:
        userid=request.POST["userid"]
        name=request.POST["name"]
        score=request.POST["score"]
        #print("data received is ",userid,name,score)
        FA=FriendsAnswer()
        
        FA.name= name
        FA.score=score      
        FA.Register=Register.objects.get(pk=userid)
        FA.save()
        data = {
                'success':True,
                'message':"Data saved",
                'data':userid
                }
        return JsonResponse(data) 
        # else:
        #     data = {
        #         'success':False,
        #         'message':"data not found",
        #         'data':"" }
        #     return JsonResponse(data)
    except Exception as ex:
        #print("error is :",ex)
        return {'message':ex}




def getFriendsAnswerbyId(request):
    try:
        id=request.GET["id"] 
        name=Register.objects.get(pk=id)
        #print("name is ",name.name)
        #dd=serializers.serialize("json",FriendsAnswer.objects.filter(Register__pk__contains=id))
        dd=serializers.serialize("json",FriendsAnswer.objects.filter(Register__pk__exact=id).order_by('score'))
        #print(dd)
        if dd!="":            
            data = {
                    'success':True,
                    'message':"Data found",
                    'name':name.name,
                    'data':dd }
            return JsonResponse(data) 
        else:
            data = {
                'success':False,
                'message':"data not found",
                'data':"" }
            return JsonResponse(data)
    except Exception as ex:
        #print("error is :",ex)
        return {'message':ex}


def Game(request):
    return render(request,'game.html')


def contact(request):
    return render(request,'contact.html')


def submitContactUs(request):
    try:
        print("request comeiiii")
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        cont=contactus()
        cont.name=name
        cont.email=email
        cont.subject=subject
        cont.message=message
        cont.save()
        data = {
                'success':True,
                'message':"data saved"
                }
        return JsonResponse(data)
    except Exception as ex:
        print('error in sigin is :',ex)
        data = {
            'success':False,
            'message':ex,
            }
        return JsonResponse(data)

