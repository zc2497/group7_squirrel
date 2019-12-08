import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
class Command(BaseCommand):
    help = 'export file'
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        squirrel  = {}
        squirrels = Squirrel.objects.all()
        with open(options['csv_file'],"w") as fp:
            fieldnames = ['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from']
            writer = csv.DictWriter(fp,delimiter = ',',fieldnames=fieldnames)
            writer.writeheader()
            for item in squirrels:
                writer.writerow({
                    'X':item.longitude,
                    'Y' :item.latitude,
                    'Unique Squirrel ID':item.unique_squirrel_id,
                    'Shift':item.shift,
                    'Date':datetime.datetime.strptime(str(item.date),'%Y-%m-%d').strftime('%m%d%Y'),#['date'][4:]+'-'+item['date'][:2]+'-'+item['date'][2:4],
                    'Age':item.age,
                    'Primary Fur Color':item.primary_fur_color,
                    'Location':item.location,
                    'Specific Location':item.specific_location,
                    'Running':item.running,
                    'Chasing':item.chasing,
                    'Climbing':item.climbing,
                    'Eating':item.eating,
                    'Foraging':item.foraging,
                    'Other Activities':item.other_activities,
                    'Kuks':item.kuks,
                    'Quaas':item.quaas,
                    'Moans':item.moans,
                    'Tail flags':item.tail_flags,
                    'Tail twitches':item.tail_twitches,
                    'Approaches':item.approaches,
                    'Indifferent':item.indifferent,
                    'Runs from':item.runs_from,
                })
