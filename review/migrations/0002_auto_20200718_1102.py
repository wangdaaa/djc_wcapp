# Generated by Django 2.2.3 on 2020-07-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewgamefiledb',
            name='image',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
