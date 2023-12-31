# Generated by Django 4.2.5 on 2023-10-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='access_token',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='spotifytoken',
            name='refresh_token',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='spotifytoken',
            name='token_type',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='vote',
            name='song_id',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]
