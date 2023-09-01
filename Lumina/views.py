from django.shortcuts import render
from . models import Company
# Create your views here.

queryset = Company.objects.all()
context = {
    'data': queryset,
}

def Chart1(request):
    return render(request, "Lumina/Country_Inten.html", context)

def Chart2(request):
    return render(request, "Lumina/Region_Like.html", context)

def Chart3(request):
    return render(request, "Lumina/Topic_Rel.html", context)

def Chart4(request):
    return render(request, "Lumina/year_like.html", context)

def TableData(request):
    return render(request, "Lumina/tables.html", context)
