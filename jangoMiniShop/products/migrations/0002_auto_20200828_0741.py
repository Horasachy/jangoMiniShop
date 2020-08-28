# Generated by Django 3.1 on 2020-08-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
