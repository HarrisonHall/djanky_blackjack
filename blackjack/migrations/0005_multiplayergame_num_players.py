# Generated by Django 2.0.4 on 2019-01-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackjack', '0004_auto_20190105_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplayergame',
            name='num_players',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]