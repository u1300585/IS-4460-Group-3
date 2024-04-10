# Generated by Django 4.2.3 on 2023-09-21 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_app.customer')),
            ],
        ),
    ]
