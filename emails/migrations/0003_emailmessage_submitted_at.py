# Generated by Django 5.1 on 2024-08-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_emailmessage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
