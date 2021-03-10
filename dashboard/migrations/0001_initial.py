# Generated by Django 3.0.6 on 2021-03-10 12:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=32)),
                ('income', models.CharField(choices=[('<500', 'Less than €500'), ('>500&<1000', 'Between €500 and €1000'), ('>1000&<2000', 'Between €1000 and €2000'), ('>2000', 'More than €2000')], max_length=32)),
                ('ownCar', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('usePT', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('ptUsageStartDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TicketSells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ticket_type', models.CharField(choices=[('single', 'single ticket'), ('monthly', 'monthly ticket'), ('other', 'other ticket')], default=None, max_length=32)),
                ('ticket_count', models.IntegerField()),
            ],
        ),
    ]