# Generated by Django 2.0.4 on 2019-01-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackjack', '0002_game_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='hit',
            field=models.BooleanField(default='True'),
        ),
    ]