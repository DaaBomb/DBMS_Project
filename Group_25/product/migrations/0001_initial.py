# Generated by Django 2.1.8 on 2019-04-17 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_desc', models.TextField(blank=True)),
                ('item_image', models.ImageField(blank=True, upload_to='Item_images')),
                ('item_price', models.IntegerField(default=0)),
                ('stock_quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_image', models.ImageField(blank=True, upload_to='category_images')),
            ],
        ),
        migrations.AddField(
            model_name='cuisine_item',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Menu'),
        ),
    ]
