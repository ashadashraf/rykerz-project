# Generated by Django 4.2.1 on 2023-07-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='piece',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
