# Generated by Django 4.2 on 2023-04-28 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=200)),
                ('deadline', models.DateField()),
                ('rasm1', models.ImageField(upload_to='media')),
                ('rasm2', models.ImageField(upload_to='media')),
                ('rasm3', models.ImageField(upload_to='media')),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.category')),
            ],
        ),
    ]
