from django.http import HttpResponse
from django.shortcuts import render

from.calculate import Student

def index(request):
    return HttpResponse("He this is new site ")


def Gender(request):
    return HttpResponse("i am 35 year old man ")
def studend_info(request):

    std1=Student("Wali Meer Muhammad", 98, 90, 95)
    sum=std1.calculate_sum()
    avg=std1.calculate_avg()

    context= {
        'std1':{'name':Student.name,'sum':sum,'avg':avg},
    }
    return render(request, 'Student_record.html', context)
# Create your views here.
