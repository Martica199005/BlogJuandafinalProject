# Generated by Django 3.0.2 on 2020-04-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_articles_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, default='1.jpg', upload_to=''),
        ),
    ]
