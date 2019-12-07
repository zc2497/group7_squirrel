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
                        longitude=item['X'],
                        latitude=item['Y'],
                        unique_squirrel_id=item['Unique Squirrel ID'],
                        shift=item['Shift'],
                        date=item['Date'][4:]+'-'+item['Date'][:2]+'-'+item['Date'][2:4],
                        age=item['Age'],
                        primary_fur_color=item['Primary Fur Color'],
                        location=item['Location'],
                        specific_location=item['Specific Location'],
                        running=item['Running'].lower().capitalize(),
                        chasing=item['Chasing'].lower().capitalize(),
                        climbing=item['Climbing'].lower().capitalize(),
                        eating=item['Eating'].lower().capitalize(),
                        foraging=item['Foraging'].lower().capitalize(),
                        other_activities=item['Other Activities'],
                        kuks=item['Kuks'].lower().capitalize(),
                        quaas=item['Quaas'].lower().capitalize(),
                        moans=item['Moans'].lower().capitalize(),
                        tail_flags=item['Tail flags'].lower().capitalize(),
                        tail_twitches=item['Tail twitches'].lower().capitalize(),
                        approaches=item['Approaches'].lower().capitalize(),
                        indifferent=item['Indifferent'].lower().capitalize(),
                        runs_from=item['Runs from'].lower().capitalize()
                        )
                squirrel.save()
