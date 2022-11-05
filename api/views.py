import imp
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import UserInput
from .serializer import Serializer
from rest_framework.response import Response
from .forms import myForm
# Create your views here.
def Api(request):
    return JsonResponse({"slackUsername":"Neon-jeff",
            "backend":True,
            "age":"22",
            "bio":"Free thinker, Robotic enthusiast, Andrew Tate"
    },safe=False)


def Calculate(request):
        if request.method=='POST':
                form=myForm(request.POST)
                if form.is_valid():
                        if form.cleaned_data['Input_Json']["operation_type"]=='addition':
                                result=form.cleaned_data['Input_Json']["x"] + form.cleaned_data['Input_Json']["y"]
                                JsonResult={
                                "slackUsername":"Neon-jeff",
                                "result":result,
                                "operation_type":form.cleaned_data['Input_Json']["operation_type"]
                                }                                
                                return JsonResponse(JsonResult)
                        if form.cleaned_data['Input_Json']["operation_type"]=='subtraction':
                                result=form.cleaned_data['Input_Json']["x"] - form.cleaned_data['Input_Json']["y"]
                                JsonResult={
                                "slackUsername":"Neon-jeff",
                                "result":result,
                                "operation_type":form.cleaned_data['Input_Json']["operation_type"]
                                }                                
                                return JsonResponse(JsonResult)
                        if form.cleaned_data['Input_Json']["operation_type"]=='multiplication':
                                result=form.cleaned_data['Input_Json']["x"] * form.cleaned_data['Input_Json']["y"]
                                JsonResult={
                                "slackUsername":"Neon-jeff",
                                "result":result,
                                "operation_type":form.cleaned_data['Input_Json']["operation_type"]
                                }                                
                                return JsonResponse(JsonResult)
                         
        form=myForm()
        return render(request,'form.html',{'form':form})
