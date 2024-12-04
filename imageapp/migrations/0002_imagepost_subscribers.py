# Generated by Django 5.1.3 on 2024-12-04 09:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribed_posts', to=settings.AUTH_USER_MODEL, verbose_name='구독자'),
        ),
    ]
