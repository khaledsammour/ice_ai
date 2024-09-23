# Generated by Django 3.2.16 on 2024-09-23 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20240923_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='websites',
            name='description_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='discount_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='features_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='img_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='is_discount',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='main_img_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='main_img_selector',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='price_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='seller_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='stuck_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='websites',
            name='title_attr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
