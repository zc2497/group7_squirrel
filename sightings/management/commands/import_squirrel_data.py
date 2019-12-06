import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
class Command(BaseCommand):
    help = 'import file'
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
            for item in data:
                squirrel = Squirrel(
                        longitude=item['x'],
                        latitude=item['y'],
                        unique_squirrel_id=item['unique_squirrel_id'],
                        shift=item['shift'],
                        date=item['date'][4:]+'-'+item['date'][:2]+'-'+item['date'][2:4],
                        age=item['age'],
                        primary_fur_color=item['primary_fur_color'],
                        location=item['location'],
                        specific_location=item['specific_location'],
                        running=item['running'].capitalize(),
                        chasing=item['chasing'].capitalize(),
                        climbing=item['climbing'].capitalize(),
                        eating=item['eating'].capitalize(),
                        foraging=item['foraging'].capitalize(),
                        other_activities=item['other_activities'],
                        kuks=item['kuks'].capitalize(),
                        quaas=item['quaas'].capitalize(),
                        moans=item['moans'].capitalize(),
                        tail_flags=item['tail_flags'].capitalize(),
                        tail_twitches=item['tail_twitches'].capitalize(),
                        approaches=item['approaches'].capitalize(),
                        indifferent=item['indifferent'].capitalize(),
                        runs_from=item['runs_from'].capitalize()
                        )
                squirrel.save()
