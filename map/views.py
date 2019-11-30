from django.shortcuts import render

from .models import Squirrel
# Create your views here.
def index(request):
    #template = loader.get_template('map/index.html')
    Squirrel_longitude = [longitude for longitude in Squirrel.objects.all()]
    Squirrel_latitude = [latitude for latitude in Squirrel.objects.all()]
    context = {'Squirrel_longitude':Squirrel_longitude,'Squirrel_latitude':Squirrel_latitude,}
    return render(request,'map/index.html',context)


# Create your views here.
