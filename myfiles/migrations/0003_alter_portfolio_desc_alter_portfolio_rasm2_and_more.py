# Generated by Django 4.2 on 2023-04-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0002_alter_portfolio_desc_alter_portfolio_rasm2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='rasm2',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='rasm3',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
