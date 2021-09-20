from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

def student_detail(request, pk):
    obj1=Student.objects.get(id=pk)
    serializer=StudentSerializer(obj1)
    return JsonResponse(serializer.data)

def student_list(request):
    obj1=Student.objects.all()
    serializer=StudentSerializer(obj1, many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def codestack_home(request):
    return render(request,'index.html')