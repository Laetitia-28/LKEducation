# Generated by Django 4.2.1 on 2023-06-14 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteVitrine', '0005_remove_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
