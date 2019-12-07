import csv
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
            fieldnames = ['x','y','unique_squirrel_id','shift','date','age','primary_fur_color','location','specific_location','running','chasing','climbing','eating','foraging','other_activities','kuks','quaas','moans','tail_flags','tail_twitches','approaches','indifferent','runs_from']
            writer = csv.DictWriter(fp,delimiter = ',',fieldnames=fieldnames)
            writer.writeheader()
            for item in squirrels:
                writer.writerow({
                    'x':item.longitude,
                    'y' :item.latitude,
                    'unique_squirrel_id':item.unique_squirrel_id,
                    'shift':item.shift,
                    'date':item.date,#['date'][4:]+'-'+item['date'][:2]+'-'+item['date'][2:4],
                    'age':item.age,
                    'primary_fur_color':item.primary_fur_color,
                    'location':item.location,
                    'specific_location':item.specific_location,
                    'running':item.running,
                    'chasing':item.chasing,
                    'climbing':item.climbing,
                    'eating':item.eating,
                    'foraging':item.foraging,
                    'other_activities':item.other_activities,
                    'kuks':item.kuks,
                    'quaas':item.quaas,
                    'moans':item.moans,
                    'tail_flags':item.tail_flags,
                    'tail_twitches':item.tail_twitches,
                    'approaches':item.approaches,
                    'indifferent':item.indifferent,
                    'runs_from':item.runs_from,
                })
