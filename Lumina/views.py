from django.shortcuts import render
from . models import Company
from .forms import DashboardFilterForm
# Create your views here.


def Chart1(request):
    queryset = Company.objects.all()
    context = {
        'data': queryset,
    }
    return render(request, "Lumina/Country_Inten.html", context)


def Chart2(request):
    queryset = Company.objects.all()
    context = {
        'data': queryset,
    }
    return render(request, "Lumina/Region_Like.html", context)


def Chart3(request):
    queryset = Company.objects.all()
    context = {
        'data': queryset,
    }
    return render(request, "Lumina/Topic_Rel.html", context)


def Chart4(request):
    queryset = Company.objects.all()
    context = {
        'data': queryset,
    }
    return render(request, "Lumina/year_like.html", context)


def TableData(request):
    queryset = Company.objects.all()
    context = {
        'data': queryset,
    }
    return render(request, "Lumina/tables.html", context)


def dashboard(request):
    # Initialize the form and the data queryset
    form = DashboardFilterForm(request.POST)
    data = Company.objects.all()  # Replace with your actual queryset

    # Apply filters based on form input
    if form.is_valid():
        if form.cleaned_data['end_year']:
            data = data.filter(end_year=form.cleaned_data['end_year'])
        if form.cleaned_data['topics']:
            data = data.filter(topics=form.cleaned_data['topics'])
        if form.cleaned_data['sector']:
            data = data.filter(sector=form.cleaned_data['sector'])
        if form.cleaned_data['region']:
            data = data.filter(region=form.cleaned_data['region'])
        if form.cleaned_data['pest']:
            data = data.filter(pest=form.cleaned_data['pest'])
        if form.cleaned_data['source']:
            data = data.filter(source=form.cleaned_data['source'])
        if form.cleaned_data['swot']:
            data = data.filter(swot=form.cleaned_data['swot'])
        if form.cleaned_data['country']:
            data = data.filter(country=form.cleaned_data['country'])
        if form.cleaned_data['city']:
            data = data.filter(city=form.cleaned_data['city'])
        # Add more filters as needed

    context = {'data': data, 'form': form}
    return render(request, 'dashboard.html', context)
