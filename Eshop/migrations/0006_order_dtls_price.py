# Generated by Django 4.0.1 on 2023-01-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0005_order_dtls'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_dtls',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]