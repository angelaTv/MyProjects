# Generated by Django 3.0.3 on 2020-03-18 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0003_remove_registertable_cpass'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoginTable',
        ),
        migrations.DeleteModel(
            name='RegisterTable',
        ),
    ]
