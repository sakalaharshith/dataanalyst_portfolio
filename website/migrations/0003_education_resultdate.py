# Generated by Django 5.1.2 on 2024-11-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='ResultDate',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
