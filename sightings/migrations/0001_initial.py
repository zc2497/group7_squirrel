# Generated by Django 3.0 on 2019-12-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(help_text='Longitude')),
                ('latitude', models.FloatField(help_text='Latitude')),
                ('unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=255)),
                ('shift', models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], default='AM', help_text='Shift', max_length=255)),
                ('date', models.DateField(help_text='Date', max_length=255)),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default='Adult', help_text='Age', max_length=255)),
                ('primary_fur_color', models.CharField(choices=[('gray', 'Gray'), ('cinnamon', 'Cinnamon'), ('black', 'Black')], default='gray', help_text='Primary Fur Color', max_length=255)),
                ('location', models.CharField(choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], default='Above Ground', help_text='Location', max_length=255)),
                ('specific_location', models.CharField(help_text='Specific Location', max_length=255)),
                ('running', models.BooleanField(help_text='Running')),
                ('chasing', models.BooleanField(help_text='Chasing')),
                ('climbing', models.BooleanField(help_text='Climbing')),
                ('eating', models.BooleanField(help_text='Eating')),
                ('foraging', models.BooleanField(help_text='Foraging')),
                ('other_activities', models.CharField(help_text='Other Activities', max_length=255)),
                ('kuks', models.BooleanField(help_text='Kuks')),
                ('quaas', models.BooleanField(help_text='Quaas')),
                ('moans', models.BooleanField(help_text='Moans')),
                ('tail_flags', models.BooleanField(help_text='Tail flags')),
                ('tail_twitches', models.BooleanField(help_text='Tail twitches')),
                ('approaches', models.BooleanField(help_text='Approaches')),
                ('indifferent', models.BooleanField(help_text='Indifferent')),
                ('runs_from', models.BooleanField(help_text='Runs from')),
            ],
        ),
    ]
