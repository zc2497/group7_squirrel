from django.shortcuts import render

from .models import Squirrel
# Create your views here.
def index(request):
    #template = loader.get_template('map/index.html')
    #context = {'Squirrel_longitude':Squirrel_longitude,'Squirrel_latitude':Squirrel_latitude,}
    try:
        context = {'Squirrel':Squirrel.objects.all()[:50]}
    except Squirrel.DoesNotExist:
        raise Http404("Squirrel does not exist")

    return render(request,'map/index.html',context)


# Create your views here.
