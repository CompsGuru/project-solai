# Generated by Django 3.2 on 2022-11-24 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks_v1', '0025_auto_20221122_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('at_tracking', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('matched', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('matched_date', models.DateTimeField(blank=True, null=True)),
                ('investors', models.ManyToManyField(related_name='trackers', to=settings.AUTH_USER_MODEL)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset', to='stocks_v1.stock')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]