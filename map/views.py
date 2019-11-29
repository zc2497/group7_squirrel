from django.shortcuts import render

from .models import Squirrel
# Create your views here.
def index(request):
    #template = loader.get_template('map/index.html')
    longitude = [longitude for longitude in Squirrel.objects.all()]
    latitude = [latitude for latitude in Squirrel.objects.all()]
    context = {longitude, latitude,}
    return render(request,'map/index.html',context)


# Create your views here.
