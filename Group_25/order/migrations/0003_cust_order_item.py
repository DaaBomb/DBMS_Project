# Generated by Django 2.1.8 on 2019-04-17 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('order', '0002_auto_20190417_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust_order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Cuisine_item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Cust_order')),
            ],
        ),
    ]