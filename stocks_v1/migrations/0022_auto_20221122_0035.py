# Generated by Django 3.2 on 2022-11-21 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_v1', '0021_auto_20221122_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalstock',
            old_name='percentage_change',
            new_name='change',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='percentage_change',
            new_name='change',
        ),
    ]
