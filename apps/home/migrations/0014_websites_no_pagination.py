# Generated by Django 3.2.16 on 2024-10-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20241007_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='websites',
            name='no_pagination',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
