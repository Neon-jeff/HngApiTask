# Generated by Django 4.1.1 on 2022-11-03 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinput',
            old_name='operation',
            new_name='operation_type',
        ),
    ]
