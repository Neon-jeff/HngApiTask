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


# def Calculate(request):
#         if request.method=='POST':
#                 form=myForm(request.POST)
#                 if form.is_valid():
#                         if form.cleaned_data['Input_Json']["operation_type"]=='addition':
#                                 result=form.cleaned_data['Input_Json']["x"] + form.cleaned_data['Input_Json']["y"]
#                                 JsonResult={
#                                 "slackUsername":"Neon-jeff",
#                                 "result":result,
#                                 "operation_type":form.cleaned_data['Input_Json']["operation_type"]
#                                 }                                
#                                 return JsonResponse(JsonResult)
#                         if form.cleaned_data['Input_Json']["operation_type"]=='subtraction':
#                                 result=form.cleaned_data['Input_Json']["x"] - form.cleaned_data['Input_Json']["y"]
#                                 JsonResult={
#                                 "slackUsername":"Neon-jeff",
#                                 "result":result,
#                                 "operation_type":form.cleaned_data['Input_Json']["operation_type"]
#                                 }                                
#                                 return JsonResponse(JsonResult)
#                         if form.cleaned_data['Input_Json']["operation_type"]=='multiplication':
#                                 result=form.cleaned_data['Input_Json']["x"] * form.cleaned_data['Input_Json']["y"]
#                                 JsonResult={
#                                 "slackUsername":"Neon-jeff",
#                                 "result":result,
#                                 "operation_type":form.cleaned_data['Input_Json']["operation_type"]
#                                 }                                
#                                 return JsonResponse(JsonResult)
                         
#         form=myForm()
#         return render(request,'form.html',{'form':form})

@api_view(['POST'])
def Operation(request):
        # operation_type=request.data['operation_type']
        DataResult={}
        serializer=Serializer(data=request.data)
        if serializer.is_valid():
                operation_type=serializer.validated_data['operation_type']
                x=serializer.validated_data['x']
                y=serializer.validated_data['y']
                if operation_type=='addition':
                        result=x+y
                if operation_type=='subtraction':
                        result=x-y
                if operation_type=='multiplication':
                        result=x*y
                DataResult={
                        "slackUsername":"Neon-jeff",
                        "result":result,
                        "operation_type":operation_type

                }
        
        return Response(DataResult)

