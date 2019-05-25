from django.shortcuts import render
from .models import EntityType, MotherEntity


# Create your views here.
def index(request):
    return render(request, 'index.html')


def entity(request, uuid):
    filteredEntities = MotherEntity.objects.filter(Type=uuid)
    return render(request, 'entities.html', {'Entities': filteredEntities})


def entities(request):
    return render(request, 'entities.html', {'Entities': MotherEntity.objects.all()})


def types(request):
    return render(request, 'types.html', {'Types': EntityType.objects.all()})

