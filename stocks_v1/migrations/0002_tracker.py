# Generated by Django 3.2 on 2022-10-01 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks_v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('in_queue', models.BooleanField(default=False)),
                ('start_date', models.DateField(auto_now=True)),
                ('last_updated', models.DateField(auto_now_add=True)),
                ('completed', models.DateField(auto_now_add=True)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset', to='stocks_v1.stock')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]