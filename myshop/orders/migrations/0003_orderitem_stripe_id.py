# Generated by Django 4.1.4 on 2023-03-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]