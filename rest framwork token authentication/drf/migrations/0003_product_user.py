# Generated by Django 4.2.9 on 2024-04-22 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import drf.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drf', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=drf.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]