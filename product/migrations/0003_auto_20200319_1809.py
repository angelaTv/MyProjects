# Generated by Django 3.0.3 on 2020-03-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_producttable_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuerySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='producttable',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producttable',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
