# Generated by Django 4.2.1 on 2023-06-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteVitrine', '0006_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
