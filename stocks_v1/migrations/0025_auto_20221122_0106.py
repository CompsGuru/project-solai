# Generated by Django 3.2 on 2022-11-22 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_v1', '0024_auto_20221122_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocktracker',
            name='investors',
        ),
        migrations.RemoveField(
            model_name='stocktracker',
            name='stock',
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={},
        ),
        migrations.AlterField(
            model_name='historicalstock',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='historicalstock',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(blank=True, max_length=55, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='PriceNotification',
        ),
        migrations.DeleteModel(
            name='StockTracker',
        ),
    ]
