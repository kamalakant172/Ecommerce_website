# Generated by Django 4.0.1 on 2023-01-05 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0003_category_cat_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=200)),
                ('price', models.IntegerField()),
                ('desc', models.TextField(max_length=1000, null=True)),
                ('product_image', models.ImageField(null=True, upload_to='upload/product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.category')),
            ],
        ),
    ]
