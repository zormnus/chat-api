# Generated by Django 4.2.5 on 2023-10-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_room_messages_room_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='uuid',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
