# Generated by Django 4.1.7 on 2023-04-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
                ('descriptions', models.TextField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('vendor', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('quantity', models.IntegerField()),
                ('original_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('categories', models.ManyToManyField(blank=True, to='shop.catagorys')),
            ],
        ),
    ]