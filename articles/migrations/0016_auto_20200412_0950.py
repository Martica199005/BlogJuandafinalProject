# Generated by Django 3.0.5 on 2020-04-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20200412_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, default='templates/logo.png', null=True, upload_to=''),
        ),
    ]
