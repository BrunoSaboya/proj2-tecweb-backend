# Generated by Django 3.2.9 on 2021-11-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.IntegerField(choices=[(0, 'Sunny'), (1, 'Rain'), (2, 'Cloudy'), (4, 'Snow')], default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
