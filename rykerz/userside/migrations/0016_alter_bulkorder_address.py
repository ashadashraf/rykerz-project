# Generated by Django 4.2.1 on 2023-07-14 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0015_alter_bulkorder_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkorder',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userside.address'),
            preserve_default=False,
        ),
    ]
