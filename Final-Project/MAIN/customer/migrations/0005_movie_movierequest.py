# Generated by Django 5.0.1 on 2024-04-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, null=True)),
                ('director', models.CharField(max_length=100, null=True)),
                ('release_year', models.CharField(max_length=50, null=True)),
                ('budget', models.CharField(max_length=50, null=True)),
                ('runtime', models.CharField(max_length=50, null=True)),
                ('rating', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='movieRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField()),
            ],
        ),
    ]
