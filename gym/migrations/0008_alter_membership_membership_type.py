# Generated by Django 3.2.4 on 2021-06-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_grouptraining_grouptrainingschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
