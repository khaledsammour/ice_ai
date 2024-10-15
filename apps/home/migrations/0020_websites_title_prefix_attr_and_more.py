# Generated by Django 4.2.9 on 2024-10-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_websites_ar_selector'),
    ]

    operations = [
        migrations.AddField(
            model_name='websites',
            name='title_prefix_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='title_prefix_selector',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='title_suffix',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='title_suffix_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='title_suffix_selector',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]