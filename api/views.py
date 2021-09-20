from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

def student_detail(request, pk):
    obj1=Student.objects.get(id=pk)
    # print(obj1)

    serializer=StudentSerializer(obj1)
    # print(serializer)

    # json_data=JSONRenderer().render(serializer.data)
    # # print(json_data)

    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    obj1=Student.objects.all()
    # print(obj1)

    serializer=StudentSerializer(obj1, many=True)
    # print(serializer)

    json_data=JSONRenderer().render(serializer.data)
    # print(json_data)

    return HttpResponse(json_data, content_type='application/json')


    def codestack_homepage(request):
        return HttpResponse(request,"This is Govind Kashyap's Site")