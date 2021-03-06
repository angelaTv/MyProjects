# Generated by Django 3.0.3 on 2020-03-30 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0002_auto_20200328_1427'),
        ('cart', '0004_auto_20200326_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')], default='created', max_length=120)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=5.99, max_digits=100)),
                ('total', models.DecimalField(decimal_places=2, default=5.99, max_digits=100)),
                ('active', models.BooleanField(default=True)),
                ('billingprofile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.BIllingProfile')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
            ],
        ),
    ]
