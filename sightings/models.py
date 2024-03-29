from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
class Squirrel(models.Model):
    longitude = models.FloatField(help_text='Longitude')
    latitude = models.FloatField(help_text='Latitude')
    unique_squirrel_id = models.CharField(help_text='Unique Squirrel ID',max_length = 255)
   # hectare = models.CharField(max_length = 255)
    PM = 'PM'
    AM = 'AM'
    shift_choices = (
            (PM,'PM'),
            (AM,'AM'),
            )
    shift = models.CharField(help_text='Shift',
            max_length=255,
            choices=shift_choices,
            default=AM,
            )
    date = models.DateField(help_text ='Date',max_length=255)
   # hectare_squirrel_number = models.IntegerField()
    adult = 'Adult'
    juvenile = 'Juvenile'
    #other = 'Other'
    age_choices = (
            (adult, 'Adult'),
            (juvenile, 'Juvenile'),
            #(other, 'Other'),
            )
    age = models.CharField(help_text='Age',
            max_length = 255,
            choices = age_choices,
            default = adult
            )
    gray,cinnamon,black='gray','cinnamon','black'
    primary_fur_color_choices=((gray,'Gray'),(cinnamon,'Cinnamon'),(black,'Black'))
    primary_fur_color = models.CharField(help_text='Primary Fur Color',
            max_length = 255,
            choices = primary_fur_color_choices,
            default = gray,
            )
    #highlight_fur_color = models.CharField(max_length = 255)
    #combination_of_primary_and_highlight_color = models.CharField(max_length = 255)
    #color_notes = models.TextField()
    above_ground='Above Ground'
    ground_plane = 'Ground Plane'
    location_choices = (
            (above_ground, 'Above Ground'),
            (ground_plane, 'Ground Plane'),
            )
    location = models.CharField(
            help_text ='Location',
            max_length = 255,
            choices = location_choices,
            default = above_ground
            )
    #above_ground_sighter_measurement = models.CharField(max_length = 255)
    specific_location = models.CharField(help_text='Specific Location',max_length = 255)
    running = models.BooleanField(help_text='Running')
    chasing = models.BooleanField(help_text='Chasing')
    climbing = models.BooleanField(help_text='Climbing')
    eating = models.BooleanField(help_text='Eating')
    foraging = models.BooleanField(help_text='Foraging')
    other_activities = models.CharField(help_text='Other Activities',max_length = 255)
    kuks = models.BooleanField(help_text='Kuks')
    quaas = models.BooleanField(help_text='Quaas')
    moans = models.BooleanField(help_text='Moans')
    tail_flags = models.BooleanField(help_text='Tail flags')
    tail_twitches = models.BooleanField(help_text='Tail twitches')
    approaches = models.BooleanField(help_text='Approaches')
    indifferent = models.BooleanField(help_text='Indifferent')
    runs_from = models.BooleanField(help_text='Runs from')
    #other_interactions = models.CharField(max_length = 255)
    #lat_long = models.CharField(max_length = 255)
    #zip_codes = models.CharField(max_length = 255)
    #community_districts = models.IntegerField()
    #borough_boundaries = models.IntegerField()
    #city_council_districts = models.IntegerField()
    #police_precincts = models.IntegerField()
    def __str__(self):
        return self.unique_squirrel_id
