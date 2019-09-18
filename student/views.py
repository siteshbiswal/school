from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . models import stud
# Create your views here.
def index(request):
    return HttpResponse("You have reached school")

def home(request):
    return HttpResponse("Sitesh is smart")

def igit(request):
    message = {"MSG":'be unique and original'}
    return JsonResponse(message)

def index1(request):
    students = stud.objects.all().filter(roll = '377046')
    context = {'students': students}
    return render(request, 'index.html', context)

def details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        sem = request.POST.get("sem")
        print(name, roll, sem)
        s = stud(naam = name, roll = int(roll), sem = int(sem))
        try:
            s.save()
        except:
            return HttpResponse("roll no. exists")
            
        return HttpResponse("your form has been submitted")
    else:
        return render(request, 'create.html')