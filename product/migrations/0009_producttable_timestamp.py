# Generated by Django 3.0.3 on 2020-03-26 08:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200325_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttable',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]