# Generated by Django 3.0.5 on 2020-04-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20200412_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='1.jpg'),
        ),
    ]
