# Generated by Django 4.2.1 on 2023-07-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='sexe',
            field=models.CharField(default='F', max_length=1),
        ),
    ]
