# Generated by Django 4.2.13 on 2024-05-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='academic_qualifications',
            field=models.CharField(default=1234, max_length=5000),
            preserve_default=False,
        ),
    ]
