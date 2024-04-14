# Generated by Django 5.0.1 on 2024-04-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_rename_homepage_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('payment_method', models.CharField(max_length=50)),
            ],
        ),
    ]
