from django.shortcuts import render

from map.models import Squirrel
# Create your views here.
def index(request):
    #template = loader.get_template('map/index.html')
    Squirrel_longitude = [longitude for longitude in Squirrel.objects.all()]
    Squirrel_latitude = [latitude for latitude in Squirrel.objects.all()]
    context = {'Squirrel_longitude':Squirrel_longitude,'Squirrel_latitude':Squirrel_latitude,}
    return render(request,'sightings/index.html',context)
def add(request):
    if request.method=="POST":
    #print("Add sightings to the databse")
        unique_squirrel_id = request.POST.get('Unique_Squirrel_ID')
        longitude = request.POST.get('Longitude')
        latitude=request.POST.get('Latitude')
        specific_location=request.POST.get('Specific_location')
        date=request.POST.get('Date')
        shift=request.POST.get('Shift')
        age=request.POST.get('Age')
        primary_fur_color=request.POST.get('Primary_fur_color')
        location=request.POST.get('Location')
        running=request.POST.get('Running')
        chasing=request.POST.get('Chasing')
        climbing=request.POST.get('Climbing')
        eating=request.POST.get('Eating')
        foraging=request.POST.get('Foraging')
        other_activities=request.POST.get('Other_Activities')
        kuks=request.POST.get('Kuks')
        quaas=request.POST.get('Quaas')
        moans=request.POST.get('Moans')
        tail_flags=request.POST.get('Tail_flags')
        tail_twitches=request.POST.get('Tail_twitches')
        approaches=request.POST.get('Approaches')
        indifferent=request.POST.get('Indifferent')

        squirrel=squirrels.objects.create(unique_squirrel_id=unique_squirrel_id,
                longitude=longitude,latitude=latitude,specific_location=specific_location,
                date=date,shift=shift,age=age,primary_fur_color=primary_fur_color,
                location=location,running=running,chasing=chasing,climbing=climbing,
                eating=eating,foraging=foraging,other_activities=other_activities,
                kuks=kuks,quaas=quaas,moans=moans,tail_flags=tail_flags,
                tail_twitches=tail_twitches,approaches=approaches, indifferent=indifferent)
        squirrel.save()
        return redirect('sightings:index')
    return render(request,'sightings/add.html')
