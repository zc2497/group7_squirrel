from django.shortcuts import render
from django.http import HttpResponse
from map.models import Squirrel
# Create your views here.
def index(request):
    #template = loader.get_template('map/index.html')
    try:
        context={'Squirrel':Squirrel.objects.all()[:50],}
    except Squirrel.DoesNotExist:
        raise Http404("Squirrel does not exist")
    return render(request,"sightings/index.html",context)
def add(request):
    if request.method=="POST":
        if request.POST.get('latitude') and request.POST.get('longitude') and request.POST.get('unique_squirrel_id'):
            squirrel=Squirrel()
            squirrel.longitude=request.POST.get('longitude')
            squirrel.latitude=request.POST.get('latitude')
            squirrel.unique_squirrel_id=request.POST.get('unique_squirrel_id')
            squirrel.shift=request.POST.get('shift')
            squirrel.date=request.POST.get('date')
            squirrel.age=request.POST.get('age')
            squirrel.primary_fur_color=request.POST.get('primary_fur_color')
            squirrel.location=request.POST.get('location')
            squirrel.specific_location=request.POST.get('specific_location')
            squirrel.running=request.POST.get('running')
            squirrel.chasing=request.POST.get('chasing')
            squirrel.climbing=request.POST.get('climbing')
            squirrel.eating=request.POST.get('eating')
            squirrel.foraging=request.POST.get('foraging')
            squirrel.other_activities=request.POST.get('other_activities')
            squirrel.kuks=request.POST.get('kuks')
            squirrel.quaas=request.POST.get('quaas')
            squirrel.moans=request.POST.get('moans')
            squirrel.tail_flags=request.POST.get('tail_flags')
            squirrel.tail_twitches=request.POST.get('tail_twitches')
            squirrel.approaches=request.POST.get('approaches')
            squirrel.indifferent=request.POST.get('indifferent')
            squirrel.runs_from=request.POST.get('runs_from')
            squirrel.save()
            return render(request,'sightings/index.html')
    else:
            return render(request,'sightings/add.html')
        #return redirect('sightings:index')

def details(request,unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    context = {'squirrel':squirrel}
    return render(request,'sightings/details.html',context)
